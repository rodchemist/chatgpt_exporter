Steps to Write and Execute a Query
Use execute_query.py as fundation.

Define Your Query
Specify the database name and a simple SQL query to test your connection.

Execute the Query
Use the connect_to_database function to establish a connection and execute your query using the provided execute_query function.

4. Follow "The Pragmatic Programmer" Guide:

Emphasize writing clean, maintainable code by following these best practices:

Use Meaningful Names: Choose clear, descriptive names for variables, functions, and classes.
Keep Code DRY (Don't Repeat Yourself): Avoid redundancy by reusing code through functions and modules.
Write Small Functions: Break down complex tasks into smaller, manageable functions.
Use Version Control: Track changes and collaborate using version control systems like Git.
Refactor Regularly: Continuously improve the code structure and readability without changing its behavior.
5. Adopt "The Zen of Python":

Use the principles in the Zen of Python as a mantra for writing Pythonic code:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
Special cases aren't special enough to break the rules.
To view the complete Zen of Python, use:

python
Copy code
import this
6. Use "Storytelling with Data":

Enhance your data communication skills by presenting data effectively:

Know Your Audience: Tailor the data presentation to the audience's level of understanding and interest.
Focus on Key Messages: Highlight the most important insights and conclusions.
Use Visuals Wisely: Incorporate charts, graphs, and other visual aids to make complex data more accessible.
Tell a Story: Structure the data presentation in a narrative format to engage and inform your audience effectively.
Be Clear and Concise: Avoid unnecessary details and jargon to maintain clarity.
7. Rewriting and Refactoring:

Always rewrite the full definition when you fix the code. If the code needs to be reorganized, rewrite it in full to maintain clarity and coherence.


# Explanation of database correspondences

"""
| System  | Server   | MSSQL Key       | Database Name            |
|---------|----------|-----------------|--------------------------|
| MSSQL   | MSSQL1   | MSSQL1_DB1_NAME | OCSDB                    |
| MSSQL   | MSSQL1   | MSSQL1_DB2_NAME | OCSDLG_Temp              |
| MSSQL   | MSSQL1   | MSSQL1_DB3_NAME | OCSDLG                   |
| MSSQL   | MSSQL1   | MSSQL1_DB4_NAME | OCSHDK                   |
| MSSQL   | MSSQL2   | MSSQL2_DB1_NAME | data_rod                 |
| MSSQL   | MSSQL2   | MSSQL2_DB2_NAME | ignition                 |
| MSSQL   | MSSQL3   | MSSQL3_DB1_NAME | BCI.Core.Batching        |
| MySQL   | MYSQL1   | MYSQL1_DB       | researchdb               |
| MySQL   | MYSQL_AI | MYSQL_AI_DB1_NAME| ai_ocsdb                 |
| MySQL   | MYSQL_AI | MYSQL_AI_DB2_NAME| ci_change_management     |
| MySQL   | MYSQL_AI | MYSQL_AI_DB3_NAME| ai_ocs_history           |
| MySQL   | MYSQL_ROD| MYSQL_ROD_DB1_NAME| rod_crypto               |
| MySQL   | MYSQL_ROD| MYSQL_ROD_DB2_NAME| rod_mysql                |
| MongoDB | -        | MONGODB_URI     | ci_mongodb               |
"""

