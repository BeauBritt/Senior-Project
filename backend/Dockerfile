# 1. Base image
FROM node:20 AS build

# 2. Set working directory
WORKDIR /app

# 3. Copy package.json and package-lock.json
COPY package*.json ./

# 4. Install dependencies (including devDependencies like typescript)
RUN npm install

# 5. Copy the rest of the source code
COPY . .

# 6. Build the TypeScript code
RUN npm run build

# 7. Final production image
FROM node:20 AS production

WORKDIR /app

# Only copy what's needed for running the app
COPY package*.json ./
RUN npm install --omit=dev

COPY --from=build /app/dist ./dist

# Copy any assets like .env.production if needed
# COPY .env.production .env

CMD ["node", "dist/index.js"]
