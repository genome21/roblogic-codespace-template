# Getting Started Guide: Forking and Loading the Roblogic Codespace Template

This guide will help you get started with the Roblogic Codespace Template by forking the repository and loading the `.devcontainer/devcontainer.json` configuration into your GitHub Codespace.

## Prerequisites

- A GitHub account
- Access to [GitHub Codespaces](https://github.com/features/codespaces) (may require a subscription or waiting for the beta access)

## Step 1: Fork the Repository

1. Visit the Roblogic Codespace Template repository at https://github.com/genome21/roblogic-codespace-template
2. Click the "Fork" button in the top right corner of the repository page.
3. Select your GitHub account (or organization) as the destination for the fork.

Now you have your own fork of the repository under your GitHub account.

## Step 2: Create a New GitHub Codespace

1. Go to the main page of your forked repository.
2. Click the "Code" button with a green icon in the top right corner of the repository page.
3. In the dropdown menu, select "Open with Codespaces" and click the "+ New codespace" button.

GitHub will start creating a new Codespace for your repository, using the configuration specified in the `.devcontainer/devcontainer.json` file. This process might take a few minutes.

## Step 3: Load the `devcontainer.json` Configuration

Once the Codespace is created and loaded, the configuration from the `.devcontainer/devcontainer.json` file will be automatically applied to the environment. This includes the Docker image, extensions, and settings specified in the configuration file.

You can now start working with your forked repository in the Codespace environment, which is set up according to the configurations provided in the `devcontainer.json` file.

## Conclusion

You have successfully forked the Roblogic Codespace Template repository and loaded the `.devcontainer/devcontainer.json` configuration into your GitHub Codespace. You can now start working on the project using the pre-configured environment. This setup will help you maintain a consistent development environment across your team and simplify the onboarding process for new team members.