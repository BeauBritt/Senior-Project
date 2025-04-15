// src/index.ts
import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { serve } from '@hono/node-server';
import { MongoClient } from 'mongodb';
import { config } from 'dotenv';
import { userRoutes } from './userRoutes.js';
config();
const app = new Hono();
app.use('*', cors({ origin: '*', credentials: true }));
const mongoUrl = process.env.URL;
const client = new MongoClient(mongoUrl);
const db = client.db('CBPacks');
const playerCollection = db.collection('Player Data');
// Register routes from another file (like your user_bp in Flask)
app.route('/user', userRoutes);
// Base route
app.get('/', async (c) => {
    const players = await playerCollection.find({}, { projection: { _id: 0 } }).toArray();
    return c.json(players);
});
// Get 5 random players
app.get('/random_players', async (c) => {
    const players = await playerCollection.find({}, { projection: { _id: 0 } }).toArray();
    const shuffled = players.sort(() => 0.5 - Math.random());
    return c.json(shuffled.slice(0, 5));
});
// Start server
serve(app);
console.log('Server is running on http://localhost:3000');
