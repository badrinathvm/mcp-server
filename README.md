# MCP Server Basic Example

A basic implementation of a **Model Context Protocol (MCP)** server that demonstrates core functionality, including tools and resources. This guide will walk you through the steps to initialize, inspect, and integrate the server.

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Initialization](#initialization)
- [MCP Inspector](#mcp-inspector)
- [Claude Integration](#claude-integration)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (Version 3.8 or later)
- **uv CLI**

To verify your installation, run:
```bash
python --version
uv --version
```

---

### Initialization

To initialize the project, navigate to a local folder of your choice and launch your terminal (PowerShell or CMD). Then, run:

```bash
uv init mcp-server-basic
```

This will set up the project directory and install the necessary dependencies.

---

## MCP Inspector

The MCP Inspector is a tool for debugging and monitoring your server. To start the inspector, use the following command:

```bash
uv run mcp dev server/weather.py
```

This command will launch the inspector and allow you to analyze the server's behavior in real time.

---

## Claude Integration

To integrate **Claude** into your MCP server, execute the installation command:

```bash
uv run mcp install server/weather.py
```

This will enable additional AI capabilities for your server.

---

## Troubleshooting

### Common Issues

1. **`uv` Command Not Found**
   - Ensure `uv` is installed and added to your system PATH.
   - Reinstall if necessary: `pip install uv-cli`

2. **Server Script Errors**
   - Verify the file path for `server/weather.py` is correct.
   - Check for missing dependencies.

3. **Permission Issues**
   - Run the terminal as an administrator (Windows) or use `sudo` (Linux/Mac).

---

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/introduction)

---

# Note 
Make sure to create .env file and add the LLM API Keys for successful execution

**Happy Coding! 🚀**
