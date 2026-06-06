def load_data():
    file_excel = 'data_traveloka_200_playstore.xlsx' # <-- WAJIB begini, tidak boleh ada '/content/drive/...' atau 'C:/Users/...'
    df_kues = pd.read_excel(file_excel, sheet_name='Data_Kuesioner_Form')
    df_play = pd.read_excel(file_excel, sheet_name='Data_Playstore_200')
    return df_kues, df_play