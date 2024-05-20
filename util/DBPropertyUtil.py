class PropertyUtil:
    @staticmethod
    def get_property_String():
        server_name = "DESKTOP-MB0Q7BK"
        database_name = "OrderMS"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
        return conn_str
