import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Page 1")
st.write("This is Page 1 of the app. You can add your content here.")

df_ex = pd.read_csv('data_cleaned/bot_ex.csv', parse_dates=['date']).set_index('date')
df_im = pd.read_csv('data_cleaned/bot_im.csv', parse_dates=['date']).set_index('date')

# Create a two-column layout that collapses to a single column on mobile
cols = st.columns(2)

def create_value_chart(df, li_columns, str_agg_column):
    # Create the figure and add the components
    n = 12
    df = df.tail(n=n)
    idx = df.index
    fig = go.Figure(
        data=[
            go.Bar(
                name=li_columns[0], 
                x=idx, 
                y=df[li_columns[0]],
                hovertemplate='%{y:,.0f} THB Million'
            ), 
            go.Bar(
                name=li_columns[1], 
                x=idx, 
                y=df[li_columns[1]],
                hovertemplate='%{y:,.0f} THB Million'
            ), 
            go.Bar(
                name=li_columns[2], 
                x=idx, 
                y=df[li_columns[2]],
                hovertemplate='%{y:,.0f} THB Million'
            ), 
            go.Bar(
                name=li_columns[3], 
                x=idx, 
                y=df[li_columns[3]],
                hovertemplate='%{y:,.0f} THB Million'
            ), 
            go.Bar(
                name='Others', 
                x=idx, 
                y=df[str_agg_column] - df[li_columns[0]] - df[li_columns[1]] - df[li_columns[2]] - df[li_columns[3]],
                hovertemplate='%{y:,.0f} THB Million'
            ), 
            go.Scatter(
                name=str_agg_column, 
                x=idx, 
                y=df[str_agg_column], 
                mode='lines+markers', 
                line=dict(color='grey'),
                hovertemplate='%{y:,.0f} THB Million',
            )
        ]
    )

    # Customize the layout to stack the bars
    fig.update_layout(
        barmode='stack',
        bargap=0,
        bargroupgap=0,
        legend_title='Legend',
        xaxis=dict(
            tickformat='%b %y',
            tickangle=-90,
            tickmode='array',
            tickvals=df.index,
        ),
        legend=dict(
            orientation='h',   # Make the legend horizontal
            yanchor='top',     # Align the top of the legend to the specified position
            y=-0.2,            # Position the legend slightly below the chart
            xanchor='center',  # Center the legend horizontally
            x=0.5              # Center the legend below the chart
        )
    )
    
    return fig

def create_ctg_chart(df, li_columns, str_agg_column):
    df = (df - df.shift(12)).div(df[str_agg_column], axis=0)
    # Create the figure and add the components
    n = 12
    df = df.tail(n)
    idx = df.index
    fig = go.Figure(
        data=[
            go.Bar(
                name=li_columns[0], 
                x=idx, 
                y=df[li_columns[0]],
                hovertemplate='%{y:.1%}',
            ), 
            go.Bar(
                name=li_columns[1], 
                x=idx, 
                y=df[li_columns[1]],
                hovertemplate='%{y:.1%}',
            ), 
            go.Bar(
                name=li_columns[2], 
                x=idx, 
                y=df[li_columns[2]],
                hovertemplate='%{y:.1%}',
            ), 
            go.Bar(
                name=li_columns[3], 
                x=idx, 
                y=df[li_columns[3]],
                hovertemplate='%{y:.1%}',
            ), 
            go.Bar(
                name='Others', 
                x=idx, 
                y=df[str_agg_column] - df[li_columns[0]] - df[li_columns[1]] - df[li_columns[2]] - df[li_columns[3]],
                hovertemplate='%{y:.1%}',
            ), 
            go.Scatter(
                name=str_agg_column, 
                x=idx, 
                y=df[str_agg_column], 
                mode='lines+markers', 
                line=dict(color='black'),
                hovertemplate='%{y:.1%}',
            )
        ]
    )

    # Customize the layout to stack the bars
    fig.update_layout(
        barmode='relative',
        bargap=0,
        bargroupgap=0,
        legend_title='Legend',
        xaxis=dict(
            tickformat='%b %y',
            tickangle=-90,
            tickmode='array',
            tickvals=df.index,
        ),
        yaxis=dict(
            tickformat='.1%', 
        ),
        legend=dict(
            orientation='h',   # Make the legend horizontal
            yanchor='top',     # Align the top of the legend to the specified position
            y=-0.2,            # Position the legend slightly below the chart
            xanchor='center',  # Center the legend horizontally
            x=0.5              # Center the legend below the chart
        )
    )
    
    return fig

# Display the first row of charts
with cols[0]:
    st.plotly_chart(
        figure_or_data=(
            create_value_chart(
                df=df_ex, 
                li_columns=['Machinery', 'Food', 'Manufactured goods', 'Chemicals'], 
                str_agg_column='Exports'
            )
            .update_layout(
                title='Exports in THB Million',
            )
        ),
        use_container_width=True
    )
with cols[1]:
    st.plotly_chart(
        figure_or_data=(
            create_value_chart(
                df=df_im, 
                li_columns=['Machinery', 'Food', 'Manufactured goods', 'Chemicals'], 
                str_agg_column='Imports'
            )
            .update_layout(
                title='Imports in THB Million',
            )
        ), 
        use_container_width=True
    )

# Display the first row of charts
with cols[0]:
    st.plotly_chart(
        figure_or_data=(
            create_ctg_chart(
                df=df_ex, 
                li_columns=['Machinery', 'Food', 'Manufactured goods', 'Chemicals'], 
                str_agg_column='Exports'
            )
            .update_layout(
                title='Exports Contribution to Growth (%YoY)',
            )
        ),
        use_container_width=True
    )
with cols[1]:
    st.plotly_chart(
        figure_or_data=(
            create_ctg_chart(
                df=df_im, 
                li_columns=['Machinery', 'Food', 'Manufactured goods', 'Chemicals'], 
                str_agg_column='Imports'
            )
            .update_layout(
                title='Imports Contribution to Growth (%YoY)',
            )
        ), 
        use_container_width=True
    )