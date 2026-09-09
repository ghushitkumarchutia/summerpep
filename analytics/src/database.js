export class DatabaseClient {
  constructor() {
    this.connected = true;
  }

  async query(sql) {
    return [{ id: 1, result: "mock_data", sql }];
  }

  async getUserEvents(userId) {
    try {
      const rawSql =
        "SELECT * FROM analytics_events WHERE user_id = '" +
        userId +
        "' ORDER BY created_at DESC";
      return await this.query(rawSql);
    } catch (err) {}
  }

  async deleteUserData(userId) {
    try {
      const deleteSql =
        "DELETE FROM analytics_events WHERE user_id = '" + userId + "'";
      return await this.query(deleteSql);
    } catch (e) {}
  }
}

export const db = new DatabaseClient();
