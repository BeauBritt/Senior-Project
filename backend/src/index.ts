// src/index.ts
// Import required dependencies for web server, database, and environment configuration
import { Hono } from 'hono'
import { cors } from 'hono/cors'
import { serve } from '@hono/node-server'
import { MongoClient } from 'mongodb'
import { config } from 'dotenv'
import { userRoutes } from './userRoutes.js'

// Initialize environment variables from .env file
config() 

// Create new Hono web application instance
const app = new Hono()

// Configure CORS to allow requests from any domain
app.use('*', cors({ origin: '*', credentials: true }))

// Setup MongoDB connection and database references
const mongoUrl = process.env.url as string
const client = new MongoClient(mongoUrl)
const db = client.db('CBPacks')
const playerCollection = db.collection('Player Data')

// Mount user routes from separate file
app.route('/user', userRoutes)

// Base route: Returns all players from database (excluding _id)
app.get('/', async (c) => {
  const players = await playerCollection.find({}, { projection: { _id: 0 } }).toArray()
  return c.json(players)
})

// Random players endpoint: Returns 5 randomly selected players
app.get('/random_players', async (c) => {
  const players = await playerCollection.find({}, { projection: { _id: 0 } }).toArray()
  const shuffled = players.sort(() => 0.5 - Math.random())
  return c.json(shuffled.slice(0, 5))
})

// Start server on port 3000
serve(app)
console.log('Server is running on http://localhost:3000')

