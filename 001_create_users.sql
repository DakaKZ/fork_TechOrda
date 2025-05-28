CREATE TABLE IF NOT EXISTS default.users (
    id UInt32,
    name String,
    created_at DateTime
) ENGINE = MergeTree
ORDER BY id;

