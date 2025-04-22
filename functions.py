def analisar_produtos(summary_sales, top_n=5):
    df = summary_sales.reset_index()
    df['cv'] = df['std'] / df['mean']
    mais_estaveis = df.sort_values(by='cv').head(top_n)
    
    return {
        "Mais Estáveis": mais_estaveis[['Branch', 'Product line', 'cv']],
        
    }
