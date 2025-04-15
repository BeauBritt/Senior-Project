# Use an official Node image as the base for building
FROM node:20 AS builder

# Set the working directory
WORKDIR /app

# Copy only the package.json and lock file first for caching
COPY package*.json ./

# Install all dependencies including TypeScript
RUN npm install

# Copy the full source code
COPY . .

# Compile TypeScript to JavaScript
RUN npm run build

# --------------------------
# Final image for production
# --------------------------
FROM node:20

WORKDIR /app

# Copy only production deps
COPY package*.json ./
RUN npm install --omit=dev

# Copy built code from builder
COPY --from=builder /app/dist ./dist

# Start app
CMD ["node", "dist/index.js"]

