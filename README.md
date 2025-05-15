

  <h1>📦 Stock Manager</h1>

  <p>
    This is a stock management app built with <strong>Python</strong> and <strong>PostgreSQL</strong>.
    You can add products with their buying and selling prices, update inventory quantities, and manage balance automatically based on transactions.
  </p>

  <h2>🔧 Features</h2>
  <ul>
    <li>Add new products with buying and selling prices</li>
    <li>Increase or decrease product quantity through inventory</li>
    <li>Balance is updated automatically when stock is added or removed</li>
    <li>Invested money in stock is calculated</li>
    <li>All transactions are logged with product ID and amount earned or spent</li>
    <li>Search product ID by name</li>
    <li>View all products</li>
    <li>All features run through <code>main.py</code> using menu options</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
STOCK_MANAGER/
├── database/
│   ├── database_config.py
│   ├── schema.sql
│   └── schema.implementation
├── scr/
│   ├── main.py
│   ├── balance.py
│   ├── database.py
│   ├── inventory.py
│   ├── products.py
│   ├── transactions.py
│   └── tests.py
  </pre>

  <h2>⚙️ Setup</h2>
  <ol>
    <li>Make sure you have PostgreSQL installed and running</li>
    <li>Create a PostgreSQL database (e.g., <code>stock_manager</code>)</li>
    <li>Run the schema setup script:
      <pre>psql -U your_username -d stock_manager -f database/schema.sql</pre>
    </li>
    <li>Edit <code>database_config.py</code> with your DB username and password</li>
    <li>Install the required Python library:
      <pre>pip install psycopg2</pre>
    </li>
    <li>Run the program:
      <pre>python scr/main.py</pre>
    </li>
  </ol>

  <h2>🛠 Technology</h2>
  <ul>
    <li>Python 3</li>
    <li>PostgreSQL</li>
    <li>psycopg2</li>
  </ul>

  <h2>✅ Status</h2>
  <ul>
    <li>Fully working with PostgreSQL backend</li>
    <li>Includes scripts to create tables and connect to database</li>
    <li>Handles inventory, balance, and transactions</li>
  </ul>

  <p>Made with ❤️ using Python and SQL.</p>

</body>
</html>
