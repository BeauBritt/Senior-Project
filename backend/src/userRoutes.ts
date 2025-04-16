import { Hono } from 'hono'
import { zValidator } from '@hono/zod-validator'
import { z } from 'zod'
import bcrypt from 'bcryptjs'
import { MongoClient } from 'mongodb'
import { config } from 'dotenv'

config()

const mongoUrl = process.env.url as string
const client = new MongoClient(mongoUrl)
const db = client.db('CBPacks')
const userCollection = db.collection('Users')

export const userRoutes = new Hono()

// Schema for validation
const authSchema = z.object({
  username: z.string().min(1),
  password: z.string().min(1),
})

// Register Route
userRoutes.post('/register', zValidator('json', authSchema), async (c) => {
  const { username, password } = await c.req.json()

  const existingUser = await userCollection.findOne({ username })
  if (existingUser) {
    return c.json({ error: 'Username already exists' }, 400)
  }

  const hashedPassword = await bcrypt.hash(password, 10)

  await userCollection.insertOne({
    username,
    password: hashedPassword,
  })

  return c.json({ message: 'User registered successfully' }, 201)
})

// Login Route
userRoutes.post('/login', zValidator('json', authSchema), async (c) => {
  const { username, password } = await c.req.json()

  const user = await userCollection.findOne({ username })
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return c.json({ error: 'Invalid username or password' }, 401)
  }

  return c.json({ message: 'Login successful', username }, 200)
})

const savedTeamsCollection = db.collection('SavedTeams')

// Save Team Route
userRoutes.post('/save_team', async (c) => {
  const { username, team, avgOVR, players } = await c.req.json();

  if (!username || !team || !avgOVR || !players) {
    return c.json({ error: 'Missing team data' }, 400);
  }

  await savedTeamsCollection.insertOne({
    username,
    team,
    avgOVR,
    players,
    timestamp: new Date(),
  });

  return c.json({ message: 'Team saved successfully!' }, 200);
});

// Get Leaderboard
userRoutes.get('/leaderboard', async (c) => {
  const topTeams = await savedTeamsCollection
    .find({}, { projection: { _id: 0, username: 1, avgOVR: 1 } })
    .sort({ avgOVR: -1 })
    .limit(10)
    .toArray();

  return c.json(topTeams);
});

// Get User's Teams
userRoutes.get('/user_teams/:username', async (c) => {
  const username = c.req.param('username');
  
  const userTeams = await savedTeamsCollection
    .find({ username }, { projection: { _id: 0 } })
    .sort({ timestamp: -1 })
    .toArray();

  if (!userTeams.length) {
    return c.json({ error: 'No teams found for this user' }, 404);
  }

  return c.json(userTeams);
});

