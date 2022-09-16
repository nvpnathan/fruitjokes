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
```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
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
docker-compose up -d
```
### System Requirements

:bulb: Before you begin, make sure you have all the below installed:

- [Python v3.10](https://python.org/)
- [Docker](https://docs.docker.com/desktop/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/)


### Initializing all the packages

1. Execute the following commands in the project root folder:
2. 
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
