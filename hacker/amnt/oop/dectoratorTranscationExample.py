def transactional(session):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                print("BEGIN TRANSACTION")
                result = func(*args, **kwargs)
                session.commit()
                print("COMMIT")
                return result
            except Exception as e:
                session.rollback()
                print("ROLLBACK")
                raise e
        return wrapper
    return decorator

class FakeSession:
    def commit(self):
        print("DB Commit")

    def rollback(self):
        print("DB Rollback")

db_session = FakeSession()

@transactional(db_session)
def update_account():
    print("Updating account")
    # simulate error
    raise ValueError("Something went wrong")

try:
    update_account()
except Exception as e:
    print(f"Error: {e}")

