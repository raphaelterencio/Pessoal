import json
import os
import pandas as pd

class ExcelPipeline:
    def open_spider(self, spider):
        if not hasattr(self, 'data'):
            with open('products.json', 'r', encoding='utf-8') as f:
                products = json.load(f)
            self.data = {
                p['id']: {
                    'Id do produto':       p['id'],
                    'nome':                p['name'],
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
        pid = item.get('produto_id')
        if pid in self.data:
            rec = self.data[pid]
            for k, v in item.items():
                if k.startswith('preco_') or k.startswith('url_'):
                    rec[k] = v
        return item

    def close_spider(self, spider):
        # Gera o Excel sempre que uma spider fechar
        excel_file = 'precos_report.xlsx'
        if os.path.exists(excel_file):
            os.remove(excel_file)

        df = pd.DataFrame(self.data.values())
        lojas = ['amazon', 'epoca', 'mercadolivre', 'pacheco', 'raia']
        df['média'] = df[[f'preco_{l}' for l in lojas]].mean(axis=1)
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
        df = df.rename(columns={f'preco_{l}': f'valor_{l}' for l in lojas})
        cols = ['Id do produto', 'nome'] + [f'valor_{l}' for l in lojas] + ['média']
        df = df[cols]

        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Preços')
        spider.logger.info(f"Arquivo {excel_file} gerado com sucesso.")
