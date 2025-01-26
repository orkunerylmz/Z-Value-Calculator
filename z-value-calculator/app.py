import streamlit as st
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align: center; color: white;'>Z VALUE CALCULATOR</h1>", unsafe_allow_html=True)

calculation_type = st.selectbox("Please Select:", 
                                ["Probability for Z", "Probability According to Z", "Probability from 0 to Z", "Probability from Z₁ to Z₂"])


# Probability for Z
if calculation_type == "Probability for Z":
    z = st.number_input("Z Value:", value=0.0, step=0.01, format="%.2f")

    table1 = norm.cdf(z)
    value1 = round(table1, 4)   
    
    st.write(f"P(Z = {z:.2f}) = {value1}")  # P(Z = z)
    
    z_values = np.arange(-3.49, 3.50, 0.01) # z values
    z_output = norm.cdf(z_values) # p values

    z_p_list = [(z, p) for z, p in zip(z_values, z_output)] # z and p values in list
    
    z_list = [z for z, p in z_p_list]   # z values in list     
    z_list_update = [float(z) for z in z_list]  # z values in float  

    p_list = [p for z, p in z_p_list]   # p values in list   
    p_list_update = [float(z) for z in p_list]  # p values in float  

    rounded_z_list = [round(num,2) for num in z_list_update]    # z values rounded
    rounded_p_list = [round(num,4) for num in p_list_update]    # p values rounded

    y_values = norm.pdf(z_values)   # p values   


    # z graph and cdf graph
    st.subheader("Normal Distribution and Cumulative Distribution Function")    # title
    
    fig, ax = plt.subplots( figsize=(8, 6))   # figure size

    ax.fill_between(z_values, y_values, 0, where=(z_values <= z), color="red", alpha=0.5, label=f"Z ≤ {z}") # fill between
    
    ax.plot(z_values, y_values, color = "red")  # plot
    ax.plot(rounded_z_list, rounded_p_list, color = "blue") # plot

    ax.grid(True, which='both', linestyle='--', linewidth=0.5)  # grid

    ax.set_title("Normal Distribution and Cumulative Distribution Function")    # title
    
    ax.set_xlabel("Z VALUES")   # x label
    ax.set_ylabel("PROBABILITY VALUES")  # y label

    ax.axhline(y=table1, color='purple', linestyle='--', label=f"P(Z ≤ {z}) = {value1}")    # horizontal line
    ax.axvline(x=z, color="green", linestyle="--", label=f"Z = {z}")    # vertical line
    ax.axhline(y=0, color='black', lw=1)    # horizontal line

    ax.legend([ f"P(Z ≤ {z:.2f})", "PDF", "CDF", f"P({z:.2f}) = {value1:.4f}", f"Z = {z:.2f}"])   # legend

    ax.set_xticks(np.arange(-3.5, 3.6, 0.5))    # x ticks
    ax.set_yticks(np.arange(0, 1.1, 0.1))   # y ticks

    st.pyplot(fig)  # plot


    # z graph
    st.subheader("Normal Distribution Function")

    fig_pdf, ax_pdf = plt.subplots(figsize=(8, 6))
           
    ax_pdf.fill_between(z_values, y_values, 0, where=(z_values <= z), color="red", alpha=0.5, label=f"Z ≤ {z}")
    
    ax_pdf.plot(z_values, y_values, color = "red")
    
    ax_pdf.set_title("Normal Distribution Function")    
    ax_pdf.set_xlabel("Z VALUES")
    
    ax_pdf.axvline(x=z, color="green", linestyle="--", label=f"Z = {z}")
    ax_pdf.axhline(0, color='black', lw=1)
    
    ax_pdf.legend([f"P(Z ≤ {z:.2f})", "PDF", f"Z = {z:.2f}"])
    
    ax_pdf.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    ax_pdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
    
    ax_pdf.set_yticks(np.arange(0, 0.51, 0.05))
    st.pyplot(fig_pdf)


    # cdf graph
    st.subheader("Cumulative Distribution Function")

    fig_cdf, ax_cdf = plt.subplots(figsize=(8, 6))

    ax_cdf.plot(rounded_z_list, rounded_p_list, color = "blue")

    ax_cdf.set_title("Cumulative Distribution Function")
    
    ax_cdf.set_xlabel("Z VALUES")
    
    ax_cdf.axvline(x=z, color="green", linestyle="--", label=f"Z = {z}")
    ax_cdf.axhline(y=table1, color='purple', linestyle='--', label=f"P(Z ≤ {z}) = {value1}")
    ax_cdf.axhline(0, color='black', lw=1)
    
    
    ax_cdf.legend(["CDF", f"Z = {z:.2f}", f"P(Z ≤ {z:.2f}) = {value1:.4f}"])
    
    ax_cdf.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    ax_cdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
    ax_cdf.set_yticks(np.arange(0, 1.1, 0.1))
    
    st.pyplot(fig_cdf)


# Probability According to Z
elif calculation_type == "Probability According to Z":
    p = st.number_input("Probability Value:", min_value=0.0, max_value=1.0, value=0.5, step=0.0001, format="%.4f")
    
    table2 = norm.ppf(p)
    value2 = round(table2, 2)
    
    st.write(f"Z = {value2} for Probability = {p:.4f}")

    z_values = np.arange(-3.49, 3.50, 0.01) # z values
    z_output = norm.cdf(z_values) # p values

    z_p_list = [(z, p) for z, p in zip(z_values, z_output)] # z and p values in list
    
    z_list = [z for z, p in z_p_list]  
    z_list_update = [float(z) for z in z_list] 
    
    p_list = [p for z, p in z_p_list]   
    p_list_update = [float(z) for z in p_list]  

    rounded_z_list = [round(num,2) for num in z_list_update]    # z values rounded
    rounded_p_list = [round(num,4) for num in p_list_update]    # p values rounded

    y_values = norm.pdf(z_values)   

    st.subheader("Normal Distribution and Cumulative Distribution Function")
    
    fig, ax = plt.subplots( figsize=(8, 6))   
    
    ax.fill_between(z_values, y_values, 0, where=(z_values <= value2), color="red", alpha=0.5, label=f"Z ≤ {value2}")
    
    ax.plot(z_values, y_values, color = "red") 
    ax.plot(rounded_z_list, rounded_p_list, color = "blue")
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    ax.set_title("Normal Distribution and Cumulative Distribution Function")
    
    ax.set_xlabel("Z VALUES")
    ax.set_ylabel("PROBABILITY VALUES")
    
    ax.axhline(y=p, color='purple', linestyle='--', label=f"P(Z ≤ {value2}) = {p}")
    ax.axvline(x=value2, color="green", linestyle="--", label=f"Z = {value2}")
    ax.axhline(y=0, color='black', lw=1)
    
    ax.legend([ f"P(Z ≤ {value2:.2f})", "PDF", "CDF", f"P({value2:.2f}) = {p:.4f}", f"Z = {value2:.2f}"])
    
    ax.set_xticks(np.arange(-3.5, 3.6, 0.5))
    ax.set_yticks(np.arange(0, 1.1, 0.1))
    
    st.pyplot(fig)


    # z graph
    st.subheader("Normal Distribution Function")

    fig_pdf, ax_pdf = plt.subplots(figsize=(8, 6))       

    ax_pdf.fill_between(z_values, y_values, 0, where=(z_values <= value2), color="red", alpha=0.5, label=f"Z ≤ {value2}")

    ax_pdf.plot(z_values, y_values, color = "red")

    ax_pdf.set_title("Normal Distribution Function")    
    ax_pdf.set_xlabel("Z VALUES")

    ax_pdf.axvline(x=value2, color="green", linestyle="--", label=f"Z = {value2}")
    ax_pdf.axhline(0, color='black', lw=1)

    ax_pdf.legend([f"P(Z ≤ {value2:.2f})", "PDF", f"Z = {value2:.2f}"])

    ax_pdf.grid(True, which='both', linestyle='--', linewidth=0.5)

    ax_pdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
    ax_pdf.set_yticks(np.arange(0, 0.51, 0.05))

    st.pyplot(fig_pdf)


    # cdf graph
    st.subheader("Cumulative Distribution Function")

    fig_cdf, ax_cdf = plt.subplots(figsize=(8, 6))

    ax_cdf.plot(rounded_z_list, rounded_p_list, color = "blue")

    ax_cdf.set_title("Cumulative Distribution Function")
    ax_cdf.set_xlabel("Z VALUES")

    ax_cdf.axvline(x=value2, color="green", linestyle="--", label=f"Z = {value2}")
    ax_cdf.axhline(y=p, color='purple', linestyle='--', label=f"P(Z ≤ {value2}) = {p}")
    ax_cdf.axhline(0, color='black', lw=1)

    ax_cdf.legend(["CDF", f"Z = {value2:.2f}", f"P(Z ≤ {value2:.2f}) = {p:.4f}"])

    ax_cdf.grid(True, which='both', linestyle='--', linewidth=0.5)

    ax_cdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
    ax_cdf.set_yticks(np.arange(0, 1.1, 0.1))

    st.pyplot(fig_cdf)


# Probability from 0 to Z
elif calculation_type == "Probability from 0 to Z":
    z = st.number_input("Z Value:", min_value=-0.01, value=1.0, step=0.01, format="%.2f")

    table1 = norm.cdf(z)
    value1 = round(table1, 4) - 0.5

    st.write(f"P(0 ≤ Z ≤ {z:.2f}) = {value1:.4f}")
    
    z_values = np.arange(-3.49, 3.50, 0.01) # z values
    z_output = norm.cdf(z_values) # p values

    z_p_list = [(z, p) for z, p in zip(z_values, z_output)] # z and p values in list

    z_list = [z for z, p in z_p_list]  
    z_list_update = [float(z) for z in z_list]  

    p_list = [p for z, p in z_p_list]   
    p_list_update = [float(z) for z in p_list]  

    rounded_z_list = [round(num,2) for num in z_list_update]    # z values rounded
    rounded_p_list = [round(num,4) for num in p_list_update]    # p values rounded

    y_values = norm.pdf(z_values)   


    # z graph
    st.subheader("Normal Distribution Function(0 to Z)")

    fig_pdf, ax_pdf = plt.subplots(figsize=(8, 6))       

    ax_pdf.fill_between(z_values, y_values, 0, where=(z_values >= 0) & (z_values <= z), color="red", alpha=0.5, label=f"Z ≤ {z}")

    ax_pdf.plot(z_values, y_values, color = "red")

    ax_pdf.set_title("Normal Distribution Function(0 to Z)")    
    ax_pdf.set_xlabel("Z VALUES")

    ax_pdf.axvline(x=z, color="green", linestyle="--", label=f"Z = {z}")
    ax_pdf.axvline(0, color="orange",linestyle="--", label="Z = 0")
    ax_pdf.axhline(0, color='black', lw=1)

    ax_pdf.legend([f"P(0 ≤ Z ≤ {z:.2f})", "PDF", f"Z = {z:.2f}", "Z = 0"])

    ax_pdf.grid(True, which='both', linestyle='--', linewidth=0.5)

    ax_pdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
    ax_pdf.set_yticks(np.arange(0, 0.51, 0.05))

    st.pyplot(fig_pdf)




elif calculation_type == "Probability from Z₁ to Z₂":
    z1 = st.number_input("Z₁ Value:", value=-1.0, step=0.01, format="%.2f", key="z1")
    z2 = st.number_input("Z₂ Value:", value=1.0, step=0.01, format="%.2f", key="z2")

    if z1 > z2:
        st.error("Z₁ value cannot be greater than Z₂! Please check the values.")
    elif z2 < z1:
        st.error("Z₂ value cannot be less than Z₁! Please check the values.")
    else:
        st.success("Input values are appropriate.")

        value3 = round(norm.cdf(z2) - norm.cdf(z1), 4)
        st.write(f"P({z1:.2f} ≤ Z ≤ {z2:.2f}) = {value3:.4f}")
        
        z_values = np.arange(-3.49, 3.50, 0.01) # z values
        z_output = norm.cdf(z_values) # p values

        z_p_list = [(z, p) for z, p in zip(z_values, z_output)] # z and p values in list

        z_list = [z for z, p in z_p_list]  
        z_list_update = [float(z) for z in z_list]  

        p_list = [p for z, p in z_p_list]   
        p_list_update = [float(z) for z in p_list]  

        rounded_z_list = [round(num,2) for num in z_list_update]    # z values rounded
        rounded_p_list = [round(num,4) for num in p_list_update]    # p values rounded

        y_values = norm.pdf(z_values)   


        # z graph
        st.subheader("Normal Distribution Function(Z₁ to Z₂)")

        fig_pdf, ax_pdf = plt.subplots(figsize=(8, 6))       

        ax_pdf.fill_between(z_values, y_values, 0, where=(z_values >= z1) & (z_values <= z2), color="red", alpha=0.5, label=f"Z ≤ {z1}")

        ax_pdf.plot(z_values, y_values, color = "red")

        ax_pdf.set_title("Normal Distribution Function(Z₁ to Z₂)")    
        ax_pdf.set_xlabel("Z VALUES")

        ax_pdf.axvline(x=z1, color="green", linestyle="--", label=f"Z₁ = {z1}")
        ax_pdf.axvline(z2, color="orange",linestyle="--", label=f"Z₂ = {z2}")
        ax_pdf.axhline(0, color='black', lw=1)

        ax_pdf.legend([f"P({z1:.2f} ≤ Z ≤ {z2:.2f})", "PDF", f"Z₁ = {z1:.2f}", f"Z₂ = {z2:.2f}"])

        ax_pdf.grid(True, which='both', linestyle='--', linewidth=0.5)

        ax_pdf.set_xticks(np.arange(-3.5, 3.6, 0.5))
        ax_pdf.set_yticks(np.arange(0, 0.51, 0.05))

        st.pyplot(fig_pdf)

