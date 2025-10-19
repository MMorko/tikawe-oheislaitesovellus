import db

def get_threads(page, page_size):
    sql = """SELECT t.id, t.title, t.rating, t.price, COUNT(m.id) total, MAX(m.sent_at) last
             FROM threads t LEFT JOIN messages m
             ON t.id = m.thread_id
             GROUP BY t.id
             ORDER BY COALESCE(MAX(m.sent_at), t.id) DESC
             LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])


def get_thread(thread_id):
    sql = """SELECT t.id,
                    t.title,
                    t.content,
                    t.user_id,
                    t.rating,
                    t.price,
                    u.username
                    FROM threads t, users u
                    WHERE t.id = ?"""
    result = db.query(sql, [thread_id])
    return result[0] if result else None

def get_messages(thread_id):
    sql = """SELECT m.id, m.content, m.sent_at, m.user_id, u.username
             FROM messages m, users u
             WHERE m.user_id = u.id AND m.thread_id = ?
             ORDER BY m.id"""
    return db.query(sql, [thread_id])

def get_message(message_id):
    sql = "SELECT id, content, user_id, thread_id FROM messages WHERE id = ?"
    result = db.query(sql, [message_id])
    return result[0] if result else None

def add_thread(title, content, user_id, rating, price):
    sql = "INSERT INTO threads (title, user_id, content, rating, price) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, user_id, content, rating ,price])
    thread_id = db.last_insert_id()
    return thread_id

def remove_thread(thread_id):
    sql = """DELETE FROM messages WHERE thread_id = ?"""
    db.execute(sql, [thread_id])
    sql = """DELETE FROM threads WHERE id = ?"""
    db.execute(sql, [thread_id])

def add_message(content, user_id, thread_id):
    sql = """INSERT INTO messages (content, sent_at, user_id, thread_id) VALUES
             (?, datetime('now'), ?, ?)"""
    db.execute(sql, [content, user_id, thread_id])

def update_message(message_id, content):
    sql = "UPDATE messages SET content = ? WHERE id = ?"
    db.execute(sql, [content, message_id])

def remove_message(message_id):
    sql = "DELETE FROM messages WHERE id = ?"
    db.execute(sql, [message_id])

def search(query):
    sql = """SELECT t.id AS thread_id,
                    t.title AS thread_title,
                    t.rating,
                    t.price,
                    u.username
             FROM threads t
             JOIN users u ON u.id = t.user_id
             WHERE t.title LIKE ?
             ORDER BY t.id DESC"""
    return db.query(sql, ["%" + query + "%"])

def thread_count():
    sql = """SELECT COUNT(*) FROM threads"""
    result = db.query(sql)
    return result[0][0] if result else 0

def update_thread(thread_id, content):
    sql = "UPDATE threads SET content = ? WHERE id = ?"
    db.execute(sql, [content, thread_id])