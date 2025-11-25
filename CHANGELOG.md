# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Connection pooling support
- Async client implementation
- Pipeline command support
- Transaction support (MULTI/EXEC)
- Hash operations (HSET, HGET, HGETALL)
- List operations (LPUSH, RPUSH, LPOP, RPOP)
- Set operations (SADD, SMEMBERS, SISMEMBER)
- Sorted set operations
- Pub/Sub support
- Automatic reconnection on connection loss
- SSL/TLS support

## [0.1.0] - 2025-11-25

### Added
- Initial release of Sterling Python Client
- Basic string operations:
  - `set(key, value)` - Set key-value pair
  - `get(key)` - Get value by key
  - `delete(key)` - Delete key
  - `exists(key)` - Check key existence
- TTL/Expiration support:
  - `expire(key, seconds)` - Set key expiration
  - `ttl(key)` - Get remaining TTL
- Key management:
  - `keys()` - List all keys
- Context manager support for automatic connection cleanup
- Connection configuration:
  - Custom host and port
  - `decode_responses` option for string decoding
- Type hints for better IDE support
- Zero external dependencies (stdlib only)

### Features
- Python 3.8+ support
- Simple, Sterling Client API
- Thread-safe socket operations
- Clean error handling

### Known Limitations
- No connection pooling yet
- No async support yet
- No hash, list, set, or sorted set operations
- No pub/sub functionality
- No pipeline or transaction support
- Basic error handling (improvements planned)

## [0.0.1] - 2025-11-20

### Added
- Project structure initialization
- Basic client framework
- Socket connection implementation

---

[Unreleased]: https://github.com/ghosecorp/sterling-python-client/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ghosecorp/sterling-python-client/releases/tag/v0.1.0
[0.0.1]: https://github.com/ghosecorp/sterling-python-client/releases/tag/v0.0.1
```