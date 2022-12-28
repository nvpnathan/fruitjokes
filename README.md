# Fruit Jokes

Fruit Jokes is an open‑source API . It helps professional Node.js developers develop quality Node.js applications without spending time on repetitive coding tasks.

Amplication auto-generates backend apps built with TypeScript and Node.js, and a client built with React.

# Features

- REST API built with FastAPI
- Admin UI
- Role-based access control
- Docker and docker-compose for local testing
- Swagger API for documentation

# Getting Started

You can get started with Fruit Jokes immediately on ECS Fargate. 

Alternatively you can set up a local development environment.

## Project Structure

Frontend

```
.
└── src
    ├── assets
    ├── components
    ├── router
    ├── store
    |── modules
    └── views
```

Backend

```
.
├── app
│   ├── api
│   │   └── api_v1
│   │       └── endpoints
│   ├── auth
│   ├── core
│   ├── crud
│   ├── db
│   ├── internal
│   ├── models
│   └── schemas
├── build
├── migrations
│   └── models
```

## Database Schema

```
model Jokes {
  id: Int @id
  joke: String
  viewCount: Int
  authors: Author[]
  tags: String[]
  rating: Int
}

model Author {
  id: Int @id
  name: String?
  authors: Jokes[]
}
```

## Development Environment (Local)

```bash
docker-compose up -d --build
```

## Apply the migrations:

```bash
docker-compose exec backend aerich upgrade
```

Ensure [http://localhost:5000](http://localhost:5000), [http://localhost:5000/docs](http://localhost:5000/docs), and [http://localhost:8080](http://localhost:8080) work as expected.

```
### System Requirements

:bulb: Before you begin, make sure you have all the below installed:

- [Python v3.11](https://python.org/)
- [Docker](https://docs.docker.com/desktop/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/)

# Support

## Ask a question about Fruit Jokes

You can ask questions, and participate in discussions about Fruit Jokes related topics in the Fruit Jokes Slack channel.

## Create a bug report

If you see an error message or run into an issue, please [create bug report](https://github.com/nvpnathan/fruitjokes/issues/new?assignees=&labels=type%3A%20bug&template=bug_report.md&title=). This effort is valued an it will help all Fruit Joke users.


## Submit a feature request

If you have an idea, or you're missing a capability that would make Fruit Jokes funnier and more robust, please [Submit feature request](https://github.com/nvpnathan/fruitjokes/issues/new?assignees=&labels=type%3A%20feature%20request&template=feature_request.md&title=).

If a similar feature request already exists, don't forget to leave a "+1".
If you add some more information such as your thoughts and vision about the feature, your comments will be embraced warmly :)


# Contributing

Fruit Jokes is an open-source project. We are committed to a fully transparent development process and appreciate highly any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as part of the Fruit Jokes community.

Please refer to our [Contribution Guidelines](./CONTRIBUTING.md) and [Code of Conduct](./CODE_OF_CONDUCT.md).

# Contributors ✨
