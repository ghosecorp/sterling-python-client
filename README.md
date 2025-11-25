# Python Client for Sterling

A simple, Python client for connecting to Sterling Server.

[![PyPI version](https://badge.fury.io/py/sterling.svg)](https://badge.fury.io/py/sterling)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- **Simple API**: Simple interface for familiar usage
- **Lightweight**: Zero external dependencies
- **Context Manager Support**: Clean connection handling
- **Type Hints**: Full typing support for better IDE integration
- **Thread-Safe**: Safe for concurrent usage

## Installation

### Via PyPI

```
pip install sterling
```

### Via TestPyPI

```
pip install -i https://test.pypi.org/simple/ sterling
```

### From Source

```
git clone https://github.com/ghosecorp/sterling-python-client.git
cd sterling-python-client
pip install -e .
```

## Quick Start

### Basic Usage

```
from sterling import Sterling

# Connect to Sterling Cache Server
client = Sterling(host='localhost', port=9162, decode_responses=True)

# Set a value
result = client.set('foo', 'bar')
print(result)
# True

# Get a value
value = client.get('foo')
print(value)
# bar

# Close connection
client.close()
```

### Context Manager (Recommended)

```
from sterling import Sterling

with Sterling(host='localhost', port=9162) as client:
    client.set('user:1:name', 'John')
    name = client.get('user:1:name')
    print(name)
    # John
```

## API Reference

### Connection

```
Sterling(host='localhost', port=9162, decode_responses=True)
```

**Parameters:**
- `host` (str): Server hostname (default: `'localhost'`)
- `port` (int): Server port (default: `9162`)
- `decode_responses` (bool): Decode responses to strings (default: `True`)

### Commands

#### String Operations

```
# Set a key-value pair
client.set(key, value) -> bool

# Get a value by key
client.get(key) -> Optional[str]

# Delete a key
client.delete(key) -> bool

# Check if key exists
client.exists(key) -> bool
```

#### Expiration

```
# Set expiration time in seconds
client.expire(key, seconds) -> bool

# Get remaining TTL
client.ttl(key) -> int
# Returns: -2 if key doesn't exist, -1 if no expiration, seconds remaining otherwise
```

#### Key Management

```
# Get all keys
client.keys() -> List[str]
```

## Examples

### Simple Key-Value Storage

```
from sterling import Sterling

client = Sterling()

# Store and retrieve
result = client.set('foo', 'bar')
print(result)
# True

x = client.get('foo')
print(x)
# bar
```

### Working with Expiration

```
from sterling import Sterling
import time

client = Sterling()

# Set key with expiration
client.set('temp_key', 'temporary_value')
client.expire('temp_key', 10)

ttl_value = client.ttl('temp_key')
print(ttl_value)
# 10

# Wait and check again
time.sleep(11)

expired_value = client.get('temp_key')
print(expired_value)
# None
```

### User Session Management

```
from sterling import Sterling

client = Sterling()

# Store user session data
client.set('user:1:name', 'John')
client.set('user:1:surname', 'Smith')
client.set('user:1:company', 'Sterling Corp')
client.set('user:1:age', '29')

# Set session expiration (30 minutes)
client.expire('user:1:name', 1800)
client.expire('user:1:surname', 1800)
client.expire('user:1:company', 1800)
client.expire('user:1:age', 1800)

# Retrieve user data
name = client.get('user:1:name')
surname = client.get('user:1:surname')
company = client.get('user:1:company')
age = client.get('user:1:age')

print(f"{name} {surname}, {age}, works at {company}")
# John Smith, 29, works at Sterling Corp
```

### Key Management

```
from sterling import Sterling

client = Sterling()

# Add multiple keys
client.set('user:1', 'Alice')
client.set('user:2', 'Bob')
client.set('product:100', 'Laptop')

# Get all keys
all_keys = client.keys()
print(all_keys)
# ['user:1', 'user:2', 'product:100']

# Check existence
exists = client.exists('user:1')
print(exists)
# True

# Delete key
delete_result = client.delete('user:1')
print(delete_result)
# True

exists_after = client.exists('user:1')
print(exists_after)
# False
```

### Complete Example

```
from sterling import Sterling

client = Sterling(host='localhost', port=9162, decode_responses=True)

# Store simple string
result1 = client.set('foo', 'bar')
print(result1)
# True

x = client.get('foo')
print(x)
# bar

# Check existence
exists = client.exists('foo')
print(exists)
# True

# Set with expiration
result2 = client.set('temp_key', 'temporary_value')
print(result2)
# True

expire_result = client.expire('temp_key', 10)
print(expire_result)
# True

ttl_value = client.ttl('temp_key')
print(ttl_value)
# 10

# Store multiple user fields
result3 = client.set('user:1:name', 'John')
result4 = client.set('user:1:surname', 'Smith')
result5 = client.set('user:1:company', 'Ghosecorp')
result6 = client.set('user:1:age', '29')

# Retrieve values
name = client.get('user:1:name')
surname = client.get('user:1:surname')
company = client.get('user:1:company')
age = client.get('user:1:age')

print(f"{name} {surname}, age {age}, works at {company}")
# John Smith, age 29, works at Ghosecorp

# Get all keys
all_keys = client.keys()
print(all_keys)
# ['foo', 'temp_key', 'user:1:name', 'user:1:surname', 'user:1:company', 'user:1:age']

# Delete a key
delete_result = client.delete('foo')
print(delete_result)
# True

deleted_value = client.get('foo')
print(deleted_value)
# None

# Check TTL scenarios
ttl_no_expiration = client.ttl('user:1:name')
print(ttl_no_expiration)
# -1 (no expiration set)

ttl_nonexistent = client.ttl('nonexistent')
print(ttl_nonexistent)
# -2 (key doesn't exist)

# Close connection
client.close()
```

## Multi-Language Support

Sterling Cache supports clients in multiple programming languages:

- ✅ **Python** (this repository)
- 🚧 **JavaScript/Node.js** (coming soon)
- 🚧 **Go** (coming soon)
- 🚧 **Java** (coming soon)
- 🚧 **Rust** (coming soon)
- 🚧 **C/C++** (coming soon)

Want a client in your favorite language? [Open an issue](https://github.com/ghosecorp/sterling/issues) or contribute!

## Documentation

Full documentation available at: [https://github.com/ghosecorp/sterling-python-client](https://github.com/ghosecorp/sterling-python-client/blob/main/README.md)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [sterling-server](https://github.com/ghosecorp/sterling) - Sterling Cache Server

## Support

- **Issues**: [GitHub Issues](https://github.com/ghosecorp/sterling-python-client/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ghosecorp/sterling-python-client/discussions)
- **Email**: ghosecorp@gmail.com

---

**Built with ❤️ by Ghosecorp**
```