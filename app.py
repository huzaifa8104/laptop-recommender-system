import streamlit as st
import pickle
import os
import pandas as pd

laptop_pkl = pickle.load(open('./laptop-recommender-system/laptop.pkl','rb'))
similarity = pickle.load(open('./laptop-recommender-system/similarity.pkl','rb'))
image_folder = './laptop-recommender-system/img/'

def recommend(laptop):
    laptop_index = laptop_pkl[laptop_pkl['laptop_title'] == laptop].index[0]
    distances = similarity[laptop_index]
    laptop_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:5]

    recommend_laptop_image = []
    recommended_model_name = []
    recommended_cpu = []
    recommended_ram = []
    recommended_memory = []
    recommended_gpu = []
    for i in laptop_list:
        recommend_laptop_image.append(os.path.join(image_folder, laptop_pkl.iloc[i[0]].image_title + '.jpg'))
        recommended_model_name.append(laptop_pkl.iloc[i[0]].model_name)
        recommended_cpu.append(laptop_pkl.iloc[i[0]].Cpu)
        recommended_ram.append(laptop_pkl.iloc[i[0]].Ram)
        recommended_memory.append(laptop_pkl.iloc[i[0]].Memory)
        recommended_gpu.append(laptop_pkl.iloc[i[0]].Gpu)
    return recommend_laptop_image, recommended_model_name, recommended_cpu, recommended_ram, recommended_memory, recommended_gpu



selected_laptop_name = option = st.selectbox('How would you like to be contacted?',laptop_pkl['laptop_title'].values)

if st.button('Recommend'):
    image, model_name, cpu, ram, memory, gpu = recommend(selected_laptop_name)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(image[0])
        st.write('**Model Name:**',model_name[0])
        st.write('**CPU:**',cpu[0])
        st.write('**RAM:**',ram[0])
        st.write('**Memory:**',memory[0])
        st.write('**GPU:**',gpu[0])


    with col2:
        st.image(image[1])
        st.write('**Model Name:**',model_name[1])
        st.write('**CPU:**',cpu[1])
        st.write('**RAM:**',ram[1])
        st.write('**Memory:**',memory[1])
        st.write('**GPU:**',gpu[1])

    with col3:
        st.image(image[2])
        st.write('**Model Name:**',model_name[2])
        st.write('**CPU:**',cpu[2])
        st.write('**RAM:**',ram[2])
        st.write('**Memory:**',memory[2])
        st.write('**GPU:**',gpu[2])

    with col4:
        st.image(image[3])
        st.write('**Model Name:**',model_name[3])
        st.write('**CPU:**',cpu[3])
        st.write('**RAM:**',ram[3])
        st.write('**Memory:**',memory[3])
        st.write('**GPU:**',gpu[3])

    # with col5:
        # st.image(image[4])
    #     st.write('**Model Name:**',model_name[4])
    #     st.write('**CPU:**',cpu[4])
    #     st.write('**RAM:**',ram[4])
    #     st.write('**Memory:**',memory[4])
    #     st.write('**GPU:**',gpu[4])
