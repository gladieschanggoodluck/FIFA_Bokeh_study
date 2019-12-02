# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable

def table_tab(flights):

	# Calculate summary stats for table
	carrier_stats = flights.groupby('Country')['Overall Rating'].describe()
	carrier_stats = carrier_stats.reset_index().rename(
		columns={'Country': 'airline', 'count': 'flights', '50%':'median'})

	# Round statistics for display
	carrier_stats['Country'] = carrier_stats['mean'].round(2)
	carrier_src = ColumnDataSource(carrier_stats)

	# Columns of table
	table_columns = [TableColumn(field='airline', title='Country'),
					 TableColumn(field='flights', title='Counts'),
					 TableColumn(field='min', title='Min Overall Rating'),
					 TableColumn(field='mean', title='Mean Overall Rating'),
					 TableColumn(field='median', title='Median Overall Rating'),
					 TableColumn(field='max', title='Max Overall Rating')]

	carrier_table = DataTable(source=carrier_src, 
							  columns=table_columns, width=1000)

	tab = Panel(child = carrier_table, title = 'Summary Table')

	return tab