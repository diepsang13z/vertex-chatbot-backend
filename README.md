# vertex-chatbot-backend

## Installation Instructions
```
# Step 1: Create and config .env file according to .env.sample template
cp .env.sample .env

# Step 2: Build and run app with docker-compose
docker-compose -f <docker-compose file> up --build

# Optional: Run command with docker-compose
docker-compose run --rm app sh -c '<your command>'
```