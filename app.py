"""Streamlit interface for the frozen Project 2 analysis."""
import streamlit as st

from analysis import AS_OF, TICKERS, decision, run, shift, signal, visible_output

st.set_page_config(page_title='ETF allocation readiness', layout='wide')
st.title('ETF allocation readiness')
st.caption(f'Saved decision snapshot: {AS_OF}. Education only. Investment advice is outside its scope.')
st.write('The mandate minimizes estimated annual volatility on a 5-point grid. The portfolio is fully '
         'invested and long-only, with a 7% net return hurdle, at least 40% VOO, and at most 30% VB. '
         'The baseline EEM cap is 30%. VOO is the proposed comparison benchmark.')

last_36 = st.sidebar.checkbox('Use only the last 36 monthly returns')
cost_bps = st.sidebar.number_input('Annual portfolio cost (basis points)', 0, 2000, 0, step=5)
eem_cap = st.sidebar.number_input('EEM weight cap (%)', 0, 100, 30, step=5)
haircut = st.sidebar.number_input('VOO return haircut (percentage points)', 0.0, 30.0, 0.0, step=.25)
reference = run()['Constrained']
rows = run(last_36, cost_bps, eem_cap / 100, haircut / 100)
table = []
for name, result in rows.items():
    row = {'Portfolio': name, 'Mandate': result['verdict']}
    if 'weights' in result:
        row.update({ticker: f'{weight:.2%}' for ticker, weight in zip(TICKERS, result['weights'])})
        row['Net return estimate'] = f"{result['return']:.2%}"
        row['Estimated volatility'] = f"{result['volatility']:.2%}"
    table.append(row)
st.dataframe(table, hide_index=True)
change = shift(reference, rows['Constrained'])
st.subheader(decision(change))
st.write('Largest sleeve change against the frozen base: ' +
         ('infeasible' if change is None else f'{change * 100:.2f} percentage points'))
st.caption('Stop the paper pilot if any stress yields no feasible mix or moves a sleeve by at least 15 points. Live allocation is 0%.')
start, end, momentum = signal()
st.write(f'Lagged VOO momentum: {momentum:+.2%} ({start} to {end}). The signal is a timing diagnostic.')
with st.expander('Frozen baseline and stress evidence'):
    st.markdown(visible_output())
