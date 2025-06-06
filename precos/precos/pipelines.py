import json
import pandas as pd

class ExcelPipeline:
    def open_spider(self, spider):
        # Carrega lista base de produtos
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
        # Inicializa registro para cada produto
        self.data = {
            p['id']: {
                'Id do produto':       p['id'],
                'nome':                p['name'],
                # preços e URLs vazios inicialmente
                'preco_amazon':        None,
                'url_amazon':          '',
                'preco_epoca':         None,
                'url_epoca':           '',
                'preco_mercadolivre':  None,
                'url_mercadolivre':    '',
                'preco_pacheco':       None,
                'url_pacheco':         '',
                'preco_raia':          None,
                'url_raia':            ''
            }
            for p in products
        }

    def process_item(self, item, spider):
        pid = item['produto_id']
        rec = self.data.get(pid)
        if rec is not None:
            # Atualiza apenas os campos de preço e URL e nome se necessário
            for k, v in item.items():
                if k.startswith('preco_') or k.startswith('url_') or k == 'nome':
                    rec[k] = v
        return item

    def close_spider(self, spider):
        # Converte para DataFrame
        df = pd.DataFrame(self.data.values())
        lojas = ['amazon', 'epoca', 'mercadolivre', 'pacheco', 'raia']
        # Calcula média numérica dos preços
        df['média'] = df[[f'preco_{l}' for l in lojas]].mean(axis=1)
        # Cria hyperlinks para cada preço
        for l in lojas:
            preco_col = f'preco_{l}'
            url_col   = f'url_{l}'
            def make_link(row):
                val = row[preco_col]
                url = row[url_col]
                if pd.notna(val) and url:
                    return f'=HYPERLINK("{url}", "{val:.2f}")'
                return ''
            df[preco_col] = df.apply(make_link, axis=1)
        # Renomeia colunas para valor_*
        df = df.rename(columns={f'preco_{l}': f'valor_{l}' for l in lojas})
        # Ordena colunas: Id, nome, valor_amazon...valor_raia, média
        cols = ['Id do produto', 'nome'] + [f'valor_{l}' for l in lojas] + ['média']
        df = df[cols]
        # Exporta para Excel
        with pd.ExcelWriter('precos_report.xlsx', engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Preços')
        spider.logger.info("Arquivo precos_report.xlsx gerado com sucesso.")
