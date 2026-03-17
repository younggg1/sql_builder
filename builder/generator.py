"""
SQL Builder 生成器模块
负责所有 SQL 语句的生成逻辑
"""

from typing import List, Dict, Any


class SQLGenerator:
    """SQL 语句生成器"""
    
    @staticmethod
    def select(table: str, fields: str = "*", conditions: List[Dict] = None,
             order_by: str = None, order_dir: str = "ASC", limit: str = None) -> str:
        """生成 SELECT 语句"""
        if not table:
            raise ValueError("表名不能为空")
        
        sql = f"SELECT {fields or '*'}\nFROM {table}"
        
        if conditions:
            where_clause = SQLGenerator._build_where(conditions)
            if where_clause:
                sql += f"\nWHERE {where_clause}"
        
        if order_by:
            sql += f"\nORDER BY {order_by} {order_dir}"
        
        if limit:
            sql += f"\nLIMIT {limit}"
        
        return sql
    
    @staticmethod
    def insert(table: str, fields: str, values: str) -> str:
        """生成 INSERT 语句"""
        if not table:
            raise ValueError("表名不能为空")
        if not fields or not values:
            raise ValueError("字段和值不能为空")
        
        return f"INSERT INTO {table} ({fields})\nVALUES ({values})"
    
    @staticmethod
    def update(table: str, sets: List[Dict], conditions: List[Dict] = None) -> str:
        """生成 UPDATE 语句"""
        if not table:
            raise ValueError("表名不能为空")
        if not sets:
            raise ValueError("请至少设置一个要更新的字段")
        
        set_clause = ", ".join([
            f"{s['field']} = {SQLGenerator._format_value(s['value'])}"
            for s in sets if s.get('field')
        ])
        
        sql = f"UPDATE {table}\nSET {set_clause}"
        
        if conditions:
            where_clause = SQLGenerator._build_where(conditions)
            if where_clause:
                sql += f"\nWHERE {where_clause}"
            else:
                sql += "\n-- ⚠️ 警告：没有 WHERE 条件将更新所有记录!"
        
        return sql
    
    @staticmethod
    def delete(table: str, conditions: List[Dict] = None) -> str:
        """生成 DELETE 语句"""
        if not table:
            raise ValueError("表名不能为空")
        
        sql = f"DELETE FROM {table}"
        
        if conditions:
            where_clause = SQLGenerator._build_where(conditions)
            if where_clause:
                sql += f"\nWHERE {where_clause}"
            else:
                sql += "\n-- ⚠️ 警告：没有 WHERE 条件将删除所有记录!"
        
        return sql
    
    @staticmethod
    def create_database(name: str) -> str:
        """生成 CREATE DATABASE 语句"""
        if not name:
            raise ValueError("数据库名不能为空")
        return f"CREATE DATABASE {name};"
    
    @staticmethod
    def alter_database(name: str, action: str) -> str:
        """生成 ALTER DATABASE 语句"""
        if not name:
            raise ValueError("数据库名不能为空")
        return f"ALTER DATABASE {name}\n{action};"
    
    @staticmethod
    def drop_database(name: str) -> str:
        """生成 DROP DATABASE 语句"""
        if not name:
            raise ValueError("数据库名不能为空")
        return f"DROP DATABASE {name};"
    
    @staticmethod
    def create_table(name: str, columns: List[Dict]) -> str:
        """生成 CREATE TABLE 语句"""
        if not name:
            raise ValueError("表名不能为空")
        if not columns:
            raise ValueError("请至少定义一列")
        
        col_defs = []
        for col in columns:
            if col.get('name'):
                definition = f"{col['name']} {col.get('type', 'VARCHAR')}"
                if col.get('size'):
                    definition += f"({col['size']})"
                if col.get('constraint'):
                    definition += f" {col['constraint']}"
                col_defs.append(definition)
        
        return f"CREATE TABLE {name} (\n  " + ",\n  ".join(col_defs) + "\n);"
    
    @staticmethod
    def alter_table(table_name: str, action: str, params: Dict) -> str:
        """生成 ALTER TABLE 语句"""
        if not table_name:
            raise ValueError("表名不能为空")
        
        if action == "ADD COLUMN":
            return f"ALTER TABLE {table_name}\nADD COLUMN {params.get('col_def', '')};"
        elif action == "DROP COLUMN":
            return f"ALTER TABLE {table_name}\nDROP COLUMN {params.get('column', '')};"
        elif action == "MODIFY COLUMN":
            return f"ALTER TABLE {table_name}\nMODIFY COLUMN {params.get('col_def', '')};"
        elif action == "RENAME COLUMN":
            return f"ALTER TABLE {table_name}\nRENAME COLUMN {params.get('old', '')} TO {params.get('new', '')};"
        
        return "-- 未知操作"
    
    @staticmethod
    def drop_table(name: str) -> str:
        """生成 DROP TABLE 语句"""
        if not name:
            raise ValueError("表名不能为空")
        return f"DROP TABLE {name};"
    
    @staticmethod
    def truncate_table(name: str) -> str:
        """生成 TRUNCATE TABLE 语句"""
        if not name:
            raise ValueError("表名不能为空")
        return f"TRUNCATE TABLE {name};"
    
    @staticmethod
    def create_index(name: str, table: str, columns: str) -> str:
        """生成 CREATE INDEX 语句"""
        if not name or not table or not columns:
            raise ValueError("索引信息不完整")
        return f"CREATE INDEX {name}\nON {table} ({columns});"
    
    @staticmethod
    def drop_index(name: str, table: str) -> str:
        """生成 DROP INDEX 语句"""
        if not name or not table:
            raise ValueError("索引信息不完整")
        return f"DROP INDEX {name}\nON {table};"
    
    @staticmethod
    def _format_value(value: str) -> str:
        """格式化值（数字不加引号，字符串加引号）"""
        if not value:
            return "''"
        try:
            float(value)
            return value
        except ValueError:
            return f"'{value}'"
    
    @staticmethod
    def _build_where(conditions: List[Dict]) -> str:
        """构建 WHERE 子句"""
        if not conditions:
            return ""
        
        # 过滤空条件
        valid_conditions = []
        for cond in conditions:
            field = cond.get('field', '')
            if not field:
                continue
            
            op = cond.get('op', '=')
            value = cond.get('value', '')
            logic = cond.get('logic', 'AND')
            
            # 构建条件表达式
            if op in ['IS NULL', 'IS NOT NULL']:
                expr = f"{field} {op}"
            elif op == 'LIKE':
                expr = f"{field} {op} '%{value}%'"
            elif op == 'IN':
                expr = f"{field} {op} ({value})"
            elif op == 'BETWEEN':
                expr = f"{field} {op} {value}"
            else:
                try:
                    float(value)
                    expr = f"{field} {op} {value}"
                except ValueError:
                    expr = f"{field} {op} '{value}'"
            
            valid_conditions.append({'expr': expr, 'logic': logic})
        
        if not valid_conditions:
            return ""
        
        # 构建最终 SQL，逻辑运算符放在条件之间（最后一个条件的逻辑符忽略）
        parts = []
        for i, cond in enumerate(valid_conditions):
            if i == 0:
                parts.append(cond['expr'])
            else:
                # 使用前一个条件的逻辑符连接
                prev_logic = valid_conditions[i-1]['logic']
                parts[-1] += f" {prev_logic}"
                parts.append(cond['expr'])
        
        return "\n  ".join(parts)
