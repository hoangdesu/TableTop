class TableTop:
    tableData = []
    
    def __init__(self, headerRow: list):
        self.tableData.append(headerRow)
        
        
    def add_row(self, row: list):
        self.tableData.append(row)
        
        
    # Get the longest string in a column
        
    def get_column_longest_string(self) -> list:
        longestString = len(self.tableData[0][0])
        columnMax = []
        for j in range(len(self.tableData[0])):
            for i in range(len(self.tableData)):
                if len(str(self.tableData[i][j])) > longestString:
                    longestString = len(str(self.tableData[i][j]))
                # print(str(self.tableData[i][j]),longestString)
            columnMax.append(longestString)
            longestString = len(str(self.tableData[i][0]))
        
        return columnMax
    
    
    def build_table_header(self) -> str:
        columnMax = self.get_column_longest_string()
    
        tableBorder = ''
        headerRow = ''
        
        # Build table borders, add 2 spaces left and right for the padding
        for i in range(len(columnMax)):
            tableBorder += '{plus}{minus}'.format(plus='+', 
                                                minus='-' * (columnMax[i] + 2)
            )
                                                
        tableBorder += '+\n'
        
        # Align the data center in the column
        for i in range(len(self.tableData[0])):
            headerRow += '{vertical}{leftspace}{data}{rightspace} '.format(vertical="|", 
                                                                           leftspace=" "*((columnMax[i] + 2 - len(self.tableData[0][i])) // 2),
                                                                           data=self.tableData[0][i],
                                                                           rightspace=" "*((columnMax[i] + 1 - len(self.tableData[0][i])) // 2)
            )
                                                                            
        headerRow += '|\n'
        
        return [tableBorder + headerRow + tableBorder, tableBorder]

    
    def build_table_data(self) -> str:
        columnMax = self.get_column_longest_string()
        tableCells = ''
        
        for i in range(1, len(self.tableData)):
            for j in range(len(self.tableData[i])):
                
                leftSpace = (columnMax[j] + 2 - len(str(self.tableData[i][j]))) // 2
                rightSpace = columnMax[j] + 2 - len(str(self.tableData[i][j])) - leftSpace
                
                tableCells += '{vertical}{leftspace}{data}{rightspace}'.format(vertical="|", 
                                                                        leftspace=" " * leftSpace,
                                                                        data=self.tableData[i][j],
                                                                        rightspace=" " * rightSpace
                )
            tableCells += '|\n'
            
        tableCells += self.build_table_header()[1]
                    
        return tableCells                     
                                            
    
    def __str__(self) -> str:
        tableHeader = self.build_table_header()[0]
        tableData = self.build_table_data()

        completedTable = tableHeader + tableData
        
        return completedTable
        
        

        
# Author: Hoang Nguyen
