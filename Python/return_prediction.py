{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XjOx1D1pYiDD",
        "outputId": "7aaf7e5d-d5fe-4c07-cd8d-82cead2fd5b5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Libraries imported successfully!\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "print(\"Libraries imported successfully!\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/content/returns_sustainability_dataset.csv')\n",
        "\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 256
        },
        "id": "SEKuRsMYY5fP",
        "outputId": "9b0b376a-b4ef-4663-fa59-aee48df31537"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Order_ID Product_ID   User_ID  Order_Date Product_Category  Product_Price  \\\n",
              "0  ORD00000   PROD0169  USER0195  2022-01-14         Clothing        1720.71   \n",
              "1  ORD00001   PROD0318  USER1469  2022-01-03             Toys         744.06   \n",
              "2  ORD00002   PROD0427  USER1812  2025-03-16         Clothing         983.68   \n",
              "3  ORD00003   PROD0323  USER1274  2024-11-06            Books        1855.65   \n",
              "4  ORD00004   PROD0325  USER0551  2023-06-07  Home Appliances        1770.97   \n",
              "\n",
              "   Order_Quantity  Discount_Applied Shipping_Method Payment_Method  ...  \\\n",
              "0               2             30.46        Next-Day         Wallet  ...   \n",
              "1               5             29.62        Next-Day         Wallet  ...   \n",
              "2               5             47.80         Express         Wallet  ...   \n",
              "3               2              2.90         Express            COD  ...   \n",
              "4               5             44.42         Express            COD  ...   \n",
              "\n",
              "   Return_Status Return_Reason Days_to_Return  Order_Value Return_Cost  \\\n",
              "0   Not Returned     No Return              0  2393.163468           0   \n",
              "1       Returned    Size Issue             12  2618.347140         200   \n",
              "2   Not Returned     No Return              0  2567.404800           0   \n",
              "3   Not Returned     No Return              0  3603.672300           0   \n",
              "4       Returned    Size Issue             11  4921.525630         200   \n",
              "\n",
              "   Profit_Loss  CO2_Emissions  Packaging_Waste  CO2_Saved  Waste_Avoided  \n",
              "0  2393.163468            2.0              0.4        2.0            0.4  \n",
              "1  2418.347140            2.0              1.0        0.0            0.0  \n",
              "2  2567.404800            1.5              1.0        1.5            1.0  \n",
              "3  3603.672300            1.5              0.4        1.5            0.4  \n",
              "4  4721.525630            1.5              1.0        0.0            0.0  \n",
              "\n",
              "[5 rows x 23 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a290ef33-554d-4a5d-974f-adb77c4ff986\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Order_ID</th>\n",
              "      <th>Product_ID</th>\n",
              "      <th>User_ID</th>\n",
              "      <th>Order_Date</th>\n",
              "      <th>Product_Category</th>\n",
              "      <th>Product_Price</th>\n",
              "      <th>Order_Quantity</th>\n",
              "      <th>Discount_Applied</th>\n",
              "      <th>Shipping_Method</th>\n",
              "      <th>Payment_Method</th>\n",
              "      <th>...</th>\n",
              "      <th>Return_Status</th>\n",
              "      <th>Return_Reason</th>\n",
              "      <th>Days_to_Return</th>\n",
              "      <th>Order_Value</th>\n",
              "      <th>Return_Cost</th>\n",
              "      <th>Profit_Loss</th>\n",
              "      <th>CO2_Emissions</th>\n",
              "      <th>Packaging_Waste</th>\n",
              "      <th>CO2_Saved</th>\n",
              "      <th>Waste_Avoided</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ORD00000</td>\n",
              "      <td>PROD0169</td>\n",
              "      <td>USER0195</td>\n",
              "      <td>2022-01-14</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>1720.71</td>\n",
              "      <td>2</td>\n",
              "      <td>30.46</td>\n",
              "      <td>Next-Day</td>\n",
              "      <td>Wallet</td>\n",
              "      <td>...</td>\n",
              "      <td>Not Returned</td>\n",
              "      <td>No Return</td>\n",
              "      <td>0</td>\n",
              "      <td>2393.163468</td>\n",
              "      <td>0</td>\n",
              "      <td>2393.163468</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.4</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>ORD00001</td>\n",
              "      <td>PROD0318</td>\n",
              "      <td>USER1469</td>\n",
              "      <td>2022-01-03</td>\n",
              "      <td>Toys</td>\n",
              "      <td>744.06</td>\n",
              "      <td>5</td>\n",
              "      <td>29.62</td>\n",
              "      <td>Next-Day</td>\n",
              "      <td>Wallet</td>\n",
              "      <td>...</td>\n",
              "      <td>Returned</td>\n",
              "      <td>Size Issue</td>\n",
              "      <td>12</td>\n",
              "      <td>2618.347140</td>\n",
              "      <td>200</td>\n",
              "      <td>2418.347140</td>\n",
              "      <td>2.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>ORD00002</td>\n",
              "      <td>PROD0427</td>\n",
              "      <td>USER1812</td>\n",
              "      <td>2025-03-16</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>983.68</td>\n",
              "      <td>5</td>\n",
              "      <td>47.80</td>\n",
              "      <td>Express</td>\n",
              "      <td>Wallet</td>\n",
              "      <td>...</td>\n",
              "      <td>Not Returned</td>\n",
              "      <td>No Return</td>\n",
              "      <td>0</td>\n",
              "      <td>2567.404800</td>\n",
              "      <td>0</td>\n",
              "      <td>2567.404800</td>\n",
              "      <td>1.5</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.5</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>ORD00003</td>\n",
              "      <td>PROD0323</td>\n",
              "      <td>USER1274</td>\n",
              "      <td>2024-11-06</td>\n",
              "      <td>Books</td>\n",
              "      <td>1855.65</td>\n",
              "      <td>2</td>\n",
              "      <td>2.90</td>\n",
              "      <td>Express</td>\n",
              "      <td>COD</td>\n",
              "      <td>...</td>\n",
              "      <td>Not Returned</td>\n",
              "      <td>No Return</td>\n",
              "      <td>0</td>\n",
              "      <td>3603.672300</td>\n",
              "      <td>0</td>\n",
              "      <td>3603.672300</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.4</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>ORD00004</td>\n",
              "      <td>PROD0325</td>\n",
              "      <td>USER0551</td>\n",
              "      <td>2023-06-07</td>\n",
              "      <td>Home Appliances</td>\n",
              "      <td>1770.97</td>\n",
              "      <td>5</td>\n",
              "      <td>44.42</td>\n",
              "      <td>Express</td>\n",
              "      <td>COD</td>\n",
              "      <td>...</td>\n",
              "      <td>Returned</td>\n",
              "      <td>Size Issue</td>\n",
              "      <td>11</td>\n",
              "      <td>4921.525630</td>\n",
              "      <td>200</td>\n",
              "      <td>4721.525630</td>\n",
              "      <td>1.5</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 23 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a290ef33-554d-4a5d-974f-adb77c4ff986')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a290ef33-554d-4a5d-974f-adb77c4ff986 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a290ef33-554d-4a5d-974f-adb77c4ff986');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B4fvj-hyY9I4",
        "outputId": "d337157b-1529-42c8-f3dd-17750440f13c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5000, 23)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "unBjz2gPY_Fy",
        "outputId": "b6c155c5-3844-485e-e496-856e722d4fdd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 5000 entries, 0 to 4999\n",
            "Data columns (total 23 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   Order_ID          5000 non-null   object \n",
            " 1   Product_ID        5000 non-null   object \n",
            " 2   User_ID           5000 non-null   object \n",
            " 3   Order_Date        5000 non-null   object \n",
            " 4   Product_Category  5000 non-null   object \n",
            " 5   Product_Price     5000 non-null   float64\n",
            " 6   Order_Quantity    5000 non-null   int64  \n",
            " 7   Discount_Applied  5000 non-null   float64\n",
            " 8   Shipping_Method   5000 non-null   object \n",
            " 9   Payment_Method    5000 non-null   object \n",
            " 10  User_Age          5000 non-null   int64  \n",
            " 11  User_Gender       5000 non-null   object \n",
            " 12  User_Location     5000 non-null   object \n",
            " 13  Return_Status     5000 non-null   object \n",
            " 14  Return_Reason     5000 non-null   object \n",
            " 15  Days_to_Return    5000 non-null   int64  \n",
            " 16  Order_Value       5000 non-null   float64\n",
            " 17  Return_Cost       5000 non-null   int64  \n",
            " 18  Profit_Loss       5000 non-null   float64\n",
            " 19  CO2_Emissions     5000 non-null   float64\n",
            " 20  Packaging_Waste   5000 non-null   float64\n",
            " 21  CO2_Saved         5000 non-null   float64\n",
            " 22  Waste_Avoided     5000 non-null   float64\n",
            "dtypes: float64(8), int64(4), object(11)\n",
            "memory usage: 898.6+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 805
        },
        "id": "PgUDt7khZLxQ",
        "outputId": "43c53e3f-1c64-4a57-b2f5-d9b1d1f7f1a4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Order_ID            0\n",
              "Product_ID          0\n",
              "User_ID             0\n",
              "Order_Date          0\n",
              "Product_Category    0\n",
              "Product_Price       0\n",
              "Order_Quantity      0\n",
              "Discount_Applied    0\n",
              "Shipping_Method     0\n",
              "Payment_Method      0\n",
              "User_Age            0\n",
              "User_Gender         0\n",
              "User_Location       0\n",
              "Return_Status       0\n",
              "Return_Reason       0\n",
              "Days_to_Return      0\n",
              "Order_Value         0\n",
              "Return_Cost         0\n",
              "Profit_Loss         0\n",
              "CO2_Emissions       0\n",
              "Packaging_Waste     0\n",
              "CO2_Saved           0\n",
              "Waste_Avoided       0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Order_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Product_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>User_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Order_Date</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Product_Category</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Product_Price</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Order_Quantity</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Discount_Applied</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shipping_Method</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Payment_Method</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>User_Age</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>User_Gender</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>User_Location</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Return_Status</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Return_Reason</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Days_to_Return</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Order_Value</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Return_Cost</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Profit_Loss</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CO2_Emissions</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Packaging_Waste</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CO2_Saved</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Waste_Avoided</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.duplicated().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kEB-qVovZQT_",
        "outputId": "8062e7ca-daf8-4368-a629-ea669b0c1872"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.int64(0)"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Order_Date'] = pd.to_datetime(df['Order_Date'])"
      ],
      "metadata": {
        "id": "hFlOTUMXZSlk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Order_Date'].dtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GwZEUJhWce9M",
        "outputId": "e43c70ac-2175-4b01-bf1a-9b95c87e0cb6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dtype('<M8[ns]')"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Minimum Date:\", df['Order_Date'].min())\n",
        "print(\"Maximum Date:\", df['Order_Date'].max())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CUBHTLWDchNl",
        "outputId": "9257530a-bc99-47a8-b276-c5d6bb170d29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Minimum Date: 2022-01-01 00:00:00\n",
            "Maximum Date: 2025-09-03 00:00:00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "zVVcxeebcjAe",
        "outputId": "92dcd915-6dce-4704-c5c2-f5fd0ca12302"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                       Order_Date  Product_Price  Order_Quantity  \\\n",
              "count                        5000    5000.000000     5000.000000   \n",
              "mean   2023-11-06 02:53:39.840000    1054.294740        2.997600   \n",
              "min           2022-01-01 00:00:00     100.090000        1.000000   \n",
              "25%           2022-12-03 18:00:00     580.937500        2.000000   \n",
              "50%           2023-11-12 00:00:00    1044.850000        3.000000   \n",
              "75%           2024-10-17 00:00:00    1530.835000        4.000000   \n",
              "max           2025-09-03 00:00:00    1999.800000        5.000000   \n",
              "std                           NaN     548.560406        1.400709   \n",
              "\n",
              "       Discount_Applied     User_Age  Days_to_Return  Order_Value  \\\n",
              "count       5000.000000  5000.000000     5000.000000  5000.000000   \n",
              "mean          25.011476    41.551800        9.204200  2366.996469   \n",
              "min            0.000000    18.000000        0.000000    52.165727   \n",
              "25%           12.827500    30.000000        0.000000   928.078449   \n",
              "50%           25.020000    42.000000        0.000000  1864.584054   \n",
              "75%           37.380000    54.000000       12.000000  3382.309799   \n",
              "max           50.000000    65.000000       60.000000  9827.017200   \n",
              "std           14.430681    13.890195       16.753156  1834.851991   \n",
              "\n",
              "       Return_Cost  Profit_Loss  CO2_Emissions  Packaging_Waste    CO2_Saved  \\\n",
              "count  5000.000000  5000.000000    5000.000000      5000.000000  5000.000000   \n",
              "mean     58.000000  2308.996469       1.500100         0.599520     1.066600   \n",
              "min       0.000000  -147.834273       1.000000         0.200000     0.000000   \n",
              "25%       0.000000   863.905130       1.000000         0.400000     0.000000   \n",
              "50%       0.000000  1808.077845       1.500000         0.600000     1.000000   \n",
              "75%     200.000000  3345.675860       2.000000         0.800000     1.500000   \n",
              "max     200.000000  9827.017200       2.000000         1.000000     2.000000   \n",
              "std      90.761487  1838.461511       0.410346         0.280142     0.764448   \n",
              "\n",
              "       Waste_Avoided  \n",
              "count     5000.00000  \n",
              "mean         0.42668  \n",
              "min          0.00000  \n",
              "25%          0.00000  \n",
              "50%          0.40000  \n",
              "75%          0.80000  \n",
              "max          1.00000  \n",
              "std          0.36150  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ee34a2b8-e1fc-4f5c-89ef-0d7c21460d97\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Order_Date</th>\n",
              "      <th>Product_Price</th>\n",
              "      <th>Order_Quantity</th>\n",
              "      <th>Discount_Applied</th>\n",
              "      <th>User_Age</th>\n",
              "      <th>Days_to_Return</th>\n",
              "      <th>Order_Value</th>\n",
              "      <th>Return_Cost</th>\n",
              "      <th>Profit_Loss</th>\n",
              "      <th>CO2_Emissions</th>\n",
              "      <th>Packaging_Waste</th>\n",
              "      <th>CO2_Saved</th>\n",
              "      <th>Waste_Avoided</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>5000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2023-11-06 02:53:39.840000</td>\n",
              "      <td>1054.294740</td>\n",
              "      <td>2.997600</td>\n",
              "      <td>25.011476</td>\n",
              "      <td>41.551800</td>\n",
              "      <td>9.204200</td>\n",
              "      <td>2366.996469</td>\n",
              "      <td>58.000000</td>\n",
              "      <td>2308.996469</td>\n",
              "      <td>1.500100</td>\n",
              "      <td>0.599520</td>\n",
              "      <td>1.066600</td>\n",
              "      <td>0.42668</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2022-01-01 00:00:00</td>\n",
              "      <td>100.090000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>52.165727</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>-147.834273</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2022-12-03 18:00:00</td>\n",
              "      <td>580.937500</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>12.827500</td>\n",
              "      <td>30.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>928.078449</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>863.905130</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.400000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2023-11-12 00:00:00</td>\n",
              "      <td>1044.850000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>25.020000</td>\n",
              "      <td>42.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1864.584054</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1808.077845</td>\n",
              "      <td>1.500000</td>\n",
              "      <td>0.600000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.40000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2024-10-17 00:00:00</td>\n",
              "      <td>1530.835000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>37.380000</td>\n",
              "      <td>54.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>3382.309799</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>3345.675860</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.800000</td>\n",
              "      <td>1.500000</td>\n",
              "      <td>0.80000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2025-09-03 00:00:00</td>\n",
              "      <td>1999.800000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>65.000000</td>\n",
              "      <td>60.000000</td>\n",
              "      <td>9827.017200</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>9827.017200</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>NaN</td>\n",
              "      <td>548.560406</td>\n",
              "      <td>1.400709</td>\n",
              "      <td>14.430681</td>\n",
              "      <td>13.890195</td>\n",
              "      <td>16.753156</td>\n",
              "      <td>1834.851991</td>\n",
              "      <td>90.761487</td>\n",
              "      <td>1838.461511</td>\n",
              "      <td>0.410346</td>\n",
              "      <td>0.280142</td>\n",
              "      <td>0.764448</td>\n",
              "      <td>0.36150</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ee34a2b8-e1fc-4f5c-89ef-0d7c21460d97')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ee34a2b8-e1fc-4f5c-89ef-0d7c21460d97 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ee34a2b8-e1fc-4f5c-89ef-0d7c21460d97');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"Order_Date\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"1970-01-01 00:00:00.000005\",\n        \"max\": \"2025-09-03 00:00:00\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"5000\",\n          \"2023-11-06 02:53:39.840000\",\n          \"2024-10-17 00:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Product_Price\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1540.5821971776804,\n        \"min\": 100.09,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          1054.2947399999998,\n          1530.835,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Quantity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1766.7876832636412,\n        \"min\": 1.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2.9976,\n          4.0,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Discount_Applied\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1759.5167780239353,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          25.011476000000002,\n          37.38,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"User_Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1754.4944245466768,\n        \"min\": 13.890194536465357,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          41.5518,\n          54.0,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Days_to_Return\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1762.930321736372,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          5000.0,\n          9.2042,\n          16.753156001398647\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Value\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3084.225997164471,\n        \"min\": 52.165727,\n        \"max\": 9827.0172,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2366.9964694660002,\n          3382.309799,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Return_Cost\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1742.0434385482793,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          58.0,\n          90.76148703886413,\n          0.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Profit_Loss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3124.9605314146165,\n        \"min\": -147.834273,\n        \"max\": 9827.0172,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2308.9964694660002,\n          3345.6758602500004,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CO2_Emissions\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.2917352300021,\n        \"min\": 0.41034578922336656,\n        \"max\": 5000.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          5000.0,\n          1.5001,\n          0.41034578922336656\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Packaging_Waste\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.5710201572529,\n        \"min\": 0.2,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.59952,\n          0.8,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CO2_Saved\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.4473179167537,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          5000.0,\n          1.0666,\n          2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Waste_Avoided\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.6160609086241,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          5000.0,\n          0.42668,\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Product Categories:\")\n",
        "print(df['Product_Category'].value_counts())\n",
        "\n",
        "print(\"\\nReturn Status:\")\n",
        "print(df['Return_Status'].value_counts())\n",
        "\n",
        "print(\"\\nShipping Methods:\")\n",
        "print(df['Shipping_Method'].value_counts())\n",
        "\n",
        "print(\"\\nPayment Methods:\")\n",
        "print(df['Payment_Method'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ezja8Xm1cpnm",
        "outputId": "d40b25e0-4b0f-49a0-d0b4-95a57df83aa0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Product Categories:\n",
            "Product_Category\n",
            "Clothing           1766\n",
            "Electronics        1244\n",
            "Books               762\n",
            "Toys                752\n",
            "Home Appliances     476\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Return Status:\n",
            "Return_Status\n",
            "Not Returned    3550\n",
            "Returned        1450\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Shipping Methods:\n",
            "Shipping_Method\n",
            "Next-Day    1684\n",
            "Standard    1683\n",
            "Express     1633\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Payment Methods:\n",
            "Payment_Method\n",
            "Debit Card     1277\n",
            "Wallet         1275\n",
            "Credit Card    1235\n",
            "COD            1213\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "liHsWIKGctT5",
        "outputId": "634b2032-66bf-4f5e-d761-25295fbfcfc2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                       Order_Date  Product_Price  Order_Quantity  \\\n",
              "count                        5000    5000.000000     5000.000000   \n",
              "mean   2023-11-06 02:53:39.840000    1054.294740        2.997600   \n",
              "min           2022-01-01 00:00:00     100.090000        1.000000   \n",
              "25%           2022-12-03 18:00:00     580.937500        2.000000   \n",
              "50%           2023-11-12 00:00:00    1044.850000        3.000000   \n",
              "75%           2024-10-17 00:00:00    1530.835000        4.000000   \n",
              "max           2025-09-03 00:00:00    1999.800000        5.000000   \n",
              "std                           NaN     548.560406        1.400709   \n",
              "\n",
              "       Discount_Applied     User_Age  Days_to_Return  Order_Value  \\\n",
              "count       5000.000000  5000.000000     5000.000000  5000.000000   \n",
              "mean          25.011476    41.551800        9.204200  2366.996469   \n",
              "min            0.000000    18.000000        0.000000    52.165727   \n",
              "25%           12.827500    30.000000        0.000000   928.078449   \n",
              "50%           25.020000    42.000000        0.000000  1864.584054   \n",
              "75%           37.380000    54.000000       12.000000  3382.309799   \n",
              "max           50.000000    65.000000       60.000000  9827.017200   \n",
              "std           14.430681    13.890195       16.753156  1834.851991   \n",
              "\n",
              "       Return_Cost  Profit_Loss  CO2_Emissions  Packaging_Waste    CO2_Saved  \\\n",
              "count  5000.000000  5000.000000    5000.000000      5000.000000  5000.000000   \n",
              "mean     58.000000  2308.996469       1.500100         0.599520     1.066600   \n",
              "min       0.000000  -147.834273       1.000000         0.200000     0.000000   \n",
              "25%       0.000000   863.905130       1.000000         0.400000     0.000000   \n",
              "50%       0.000000  1808.077845       1.500000         0.600000     1.000000   \n",
              "75%     200.000000  3345.675860       2.000000         0.800000     1.500000   \n",
              "max     200.000000  9827.017200       2.000000         1.000000     2.000000   \n",
              "std      90.761487  1838.461511       0.410346         0.280142     0.764448   \n",
              "\n",
              "       Waste_Avoided  \n",
              "count     5000.00000  \n",
              "mean         0.42668  \n",
              "min          0.00000  \n",
              "25%          0.00000  \n",
              "50%          0.40000  \n",
              "75%          0.80000  \n",
              "max          1.00000  \n",
              "std          0.36150  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-839c50df-a5ef-4ae5-9949-0b7a450ac44a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Order_Date</th>\n",
              "      <th>Product_Price</th>\n",
              "      <th>Order_Quantity</th>\n",
              "      <th>Discount_Applied</th>\n",
              "      <th>User_Age</th>\n",
              "      <th>Days_to_Return</th>\n",
              "      <th>Order_Value</th>\n",
              "      <th>Return_Cost</th>\n",
              "      <th>Profit_Loss</th>\n",
              "      <th>CO2_Emissions</th>\n",
              "      <th>Packaging_Waste</th>\n",
              "      <th>CO2_Saved</th>\n",
              "      <th>Waste_Avoided</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>5000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.000000</td>\n",
              "      <td>5000.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>2023-11-06 02:53:39.840000</td>\n",
              "      <td>1054.294740</td>\n",
              "      <td>2.997600</td>\n",
              "      <td>25.011476</td>\n",
              "      <td>41.551800</td>\n",
              "      <td>9.204200</td>\n",
              "      <td>2366.996469</td>\n",
              "      <td>58.000000</td>\n",
              "      <td>2308.996469</td>\n",
              "      <td>1.500100</td>\n",
              "      <td>0.599520</td>\n",
              "      <td>1.066600</td>\n",
              "      <td>0.42668</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2022-01-01 00:00:00</td>\n",
              "      <td>100.090000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>52.165727</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>-147.834273</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.200000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2022-12-03 18:00:00</td>\n",
              "      <td>580.937500</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>12.827500</td>\n",
              "      <td>30.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>928.078449</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>863.905130</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.400000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>2023-11-12 00:00:00</td>\n",
              "      <td>1044.850000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>25.020000</td>\n",
              "      <td>42.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1864.584054</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1808.077845</td>\n",
              "      <td>1.500000</td>\n",
              "      <td>0.600000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.40000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>2024-10-17 00:00:00</td>\n",
              "      <td>1530.835000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>37.380000</td>\n",
              "      <td>54.000000</td>\n",
              "      <td>12.000000</td>\n",
              "      <td>3382.309799</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>3345.675860</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>0.800000</td>\n",
              "      <td>1.500000</td>\n",
              "      <td>0.80000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>2025-09-03 00:00:00</td>\n",
              "      <td>1999.800000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>50.000000</td>\n",
              "      <td>65.000000</td>\n",
              "      <td>60.000000</td>\n",
              "      <td>9827.017200</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>9827.017200</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>NaN</td>\n",
              "      <td>548.560406</td>\n",
              "      <td>1.400709</td>\n",
              "      <td>14.430681</td>\n",
              "      <td>13.890195</td>\n",
              "      <td>16.753156</td>\n",
              "      <td>1834.851991</td>\n",
              "      <td>90.761487</td>\n",
              "      <td>1838.461511</td>\n",
              "      <td>0.410346</td>\n",
              "      <td>0.280142</td>\n",
              "      <td>0.764448</td>\n",
              "      <td>0.36150</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-839c50df-a5ef-4ae5-9949-0b7a450ac44a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-839c50df-a5ef-4ae5-9949-0b7a450ac44a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-839c50df-a5ef-4ae5-9949-0b7a450ac44a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"Order_Date\",\n      \"properties\": {\n        \"dtype\": \"date\",\n        \"min\": \"1970-01-01 00:00:00.000005\",\n        \"max\": \"2025-09-03 00:00:00\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"5000\",\n          \"2023-11-06 02:53:39.840000\",\n          \"2024-10-17 00:00:00\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Product_Price\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1540.5821971776804,\n        \"min\": 100.09,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          1054.2947399999998,\n          1530.835,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Quantity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1766.7876832636412,\n        \"min\": 1.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2.9976,\n          4.0,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Discount_Applied\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1759.5167780239353,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          25.011476000000002,\n          37.38,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"User_Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1754.4944245466768,\n        \"min\": 13.890194536465357,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          41.5518,\n          54.0,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Days_to_Return\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1762.930321736372,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          5000.0,\n          9.2042,\n          16.753156001398647\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Value\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3084.225997164471,\n        \"min\": 52.165727,\n        \"max\": 9827.0172,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2366.9964694660002,\n          3382.309799,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Return_Cost\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1742.0434385482793,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          58.0,\n          90.76148703886413,\n          0.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Profit_Loss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3124.9605314146165,\n        \"min\": -147.834273,\n        \"max\": 9827.0172,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2308.9964694660002,\n          3345.6758602500004,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CO2_Emissions\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.2917352300021,\n        \"min\": 0.41034578922336656,\n        \"max\": 5000.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          5000.0,\n          1.5001,\n          0.41034578922336656\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Packaging_Waste\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.5710201572529,\n        \"min\": 0.2,\n        \"max\": 5000.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          0.59952,\n          0.8,\n          5000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CO2_Saved\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.4473179167537,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          5000.0,\n          1.0666,\n          2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Waste_Avoided\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1767.6160609086241,\n        \"min\": 0.0,\n        \"max\": 5000.0,\n        \"num_unique_values\": 7,\n        \"samples\": [\n          5000.0,\n          0.42668,\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Product Categories:\")\n",
        "print(df['Product_Category'].value_counts())\n",
        "\n",
        "print(\"\\nReturn Status:\")\n",
        "print(df['Return_Status'].value_counts())\n",
        "\n",
        "print(\"\\nShipping Methods:\")\n",
        "print(df['Shipping_Method'].value_counts())\n",
        "\n",
        "print(\"\\nPayment Methods:\")\n",
        "print(df['Payment_Method'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4lrnTVpUcvG7",
        "outputId": "c921bf84-9c0c-487f-b951-ee72167c457d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Product Categories:\n",
            "Product_Category\n",
            "Clothing           1766\n",
            "Electronics        1244\n",
            "Books               762\n",
            "Toys                752\n",
            "Home Appliances     476\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Return Status:\n",
            "Return_Status\n",
            "Not Returned    3550\n",
            "Returned        1450\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Shipping Methods:\n",
            "Shipping_Method\n",
            "Next-Day    1684\n",
            "Standard    1683\n",
            "Express     1633\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Payment Methods:\n",
            "Payment_Method\n",
            "Debit Card     1277\n",
            "Wallet         1275\n",
            "Credit Card    1235\n",
            "COD            1213\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(6, 4))\n",
        "\n",
        "sns.countplot(data=df, x='Return_Status')\n",
        "\n",
        "plt.title('Return Status Distribution')\n",
        "plt.xlabel('Return Status')\n",
        "plt.ylabel('Number of Orders')\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 410
        },
        "id": "G8dN448Ucw90",
        "outputId": "7b8ad2e9-155e-4892-c898-1e698053bf3d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 1 Axes>"
            ],
            "image/png": "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rl276nPXiYiI6B71Gkry8/MxcuRI5OTkwMbGBj4+PkhKSkLfvn0BAIsXL4aRkRGCg4NRXFyMwMBArFy5Ulrf2NgYCQkJePPNN+Hn5wdLS0uEhIRg7ty5Uh93d3fs2rULYWFhWLp0KZo0aYLPPvsMgYGBj31/iYiIqGayu0+JHPE+JUR1g/cpITI8/5P3KSEiIiLDxlBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLLAUEJERESywFBCREREssBQQkRERLKgcyhZt24ddu3aJT2PiIiAra0tnn76aVy8eLFOiyMiIiLDoXMoWbBgAczNzQEAqampWLFiBeLi4mBvb4+wsLA6L5CIiIgMg4muK1y6dAkeHh4AgO3btyM4OBjjxo3DM888g549e9Z1fURERGQgdD5SYmVlhX/++QcAsGfPHvTt2xcA0KBBA9y+fVunsWJjY/Hkk0/C2toajo6OGDx4MM6ePavVp2fPnlAoFFqP8ePHa/XJzs5GUFAQLCws4OjoiPDwcJSVlWn1SUlJQceOHaFUKuHh4YH4+Hgd95yIiIj0SecjJX379sWYMWPQoUMHnDt3DgMGDAAAZGRkwM3NTaex9u/fj9DQUDz55JMoKyvDO++8g4CAAJw6dQqWlpZSv7Fjx2Lu3LnScwsLC+nf5eXlCAoKglqtxuHDh5GTk4ORI0fC1NQUCxYsAABkZWUhKCgI48ePx8aNG7Fv3z6MGTMGzs7OCAwM1PUlICIiIj3QOZSsWLECs2bNQnZ2Nr755hs0atQIAJCWloaXX35Zp7ESExO1nsfHx8PR0RFpaWno3r271G5hYQG1Wl3tGHv27MGpU6ewd+9eODk5oX379nj33XcRGRmJmJgYmJmZYfXq1XB3d8cHH3wAAPD09MTBgwexePFihhIiIiKZ0On0TVlZGZYtW4bIyEh899136Nevn7Rszpw5mDFjxiMVU1hYCACws7PTat+4cSPs7e3Rtm1bREVF4datW9Ky1NRUeHt7w8nJSWoLDAyERqNB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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "category_return_rate = (\n",
        "    df.groupby('Product_Category')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "category_return_rate"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "oR7bi8z-c6HQ",
        "outputId": "1ee23a3f-c045-4e3b-a1c8-09b765fdeba3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Product_Category\n",
              "Clothing           37.429219\n",
              "Home Appliances    25.630252\n",
              "Electronics        25.241158\n",
              "Toys               24.069149\n",
              "Books              22.572178\n",
              "Name: Return_Status, dtype: float64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Return_Status</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Product_Category</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Clothing</th>\n",
              "      <td>37.429219</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Home Appliances</th>\n",
              "      <td>25.630252</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Electronics</th>\n",
              "      <td>25.241158</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Toys</th>\n",
              "      <td>24.069149</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Books</th>\n",
              "      <td>22.572178</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "category_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Product Category')\n",
        "plt.xlabel('Product Category')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "fxb3ClqzdEIR",
        "outputId": "382ecf8f-9798-4709-b5de-080cf2fee03e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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BQXZ3C0pUqSIqlevrlWrVkl6fOdl7dq1atCggc2dgPz58ysgICBWn8M/RUVFadmyZapbt661j9CTnmcI2zt37kjSU5tA/Zsnz5Nbt24pJCREFSpU0J49e/5zX2OMFi9erLp168oYY3OeBAQEKCQkxHqcNWvWKFOmTKpXr551fw8Pjxj9gnbt2qWrV6+qc+fONncVateurXz58mnlypUx6ujUqVOMZa1atdKOHTtsmgjOnTtX/v7+qlSp0n++NwCJA8ECwAs1ceJErVu3TosWLdJbb72l69evy93d3br+xIkTMsbo008/tX75jH4MHDhQknT16tV4ryt79uxPXZ45c+YYXxpTp04d634LpUuX1rp167RmzRqNGjVKqVKl0q1bt2J0Qj579qz1C3Py5MmVPn166xeqkJCQ/3yd48ePKyQkRD4+PjE+t3v37sXqM3NyclKOHDlsluXJk0eSbEY5atWqlbZt26a///5b0uNQ8+jRI7333nv/+RrS/30m69ev12+//abr169r9uzZNl+apZg/k+jXy5s3b4xj5s+fX9evX1doaKiuXbumsLAw5c6dO8Z2T9s3Nq5du6Y7d+6oUKFCz7X/03h7e0uS7t69G+t9VqxYoTfeeEMeHh5KkyaN0qdPr0mTJsXqHLl27Zpu376tqVOnxjhHWrduLen//m39/fffypkzZ4xzP1euXDbPn/UzyZcvn3V9NBcXF+tFhCc1a9ZM7u7u1sAaEhKiFStWxDqsAkgc6GMB4IV6/fXXrVd8GzRooPLly6tFixY6evSokidPrqioKElSz549//Xq8j+/3MTFv80J8M8vtdGedhdDkrVD839Jly6dqlWrJkkKCAhQvnz5VKdOHY0bN049evSw1lS9enXdvHlTvXv3Vr58+eTl5aULFy4oKCjI+pk8S1RUlHx8fGzuJDzpySv/9mrevLm6d++uuXPnql+/fvruu+9UsmTJWH9pf/IzeZZ/+5nEp3/70vo8c0fEVa5cueTi4qIDBw7Eavtff/1V9erVU8WKFfX111/Lz89Prq6umjFjhubNm/ef+0efR++++64CAwOfuk2RIkVi/waeg7u7u5ycYl7TTJ06terUqaO5c+dqwIABWrRokcLDw5+rzw4AxyFYAHAYZ2dnDRs2TG+++aYmTJigPn36WK+Yu7q6/ueXz2ddyUydOrVu375ts+zh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UnXr1tX48eMdXTJesNu3b2vz5s2qU6cOf5NgI/rvwbFjxzR+/HhduHBB5cqV08cffyxJypcvn958801NmjRJ0uNw4eLiooYNG8rHx0dTpkxxZPkvH0d07MCLs2fPHpMzZ07j5ORkJkyYYF0eGRlpjDFm7969JkOGDKZBgwbm+vXrjioTr4jo884YYz799FNTuHBhkyJFClO1alUzc+ZMExoaaox53NEue/bsplWrVmbnzp2OKhcJLLrDbYcOHUzz5s1t1i1btsx4enqaMWPGGGMed+adNm2adeQ6vLoYrAHRov+m7Nu3z6RPn940aNDANG/e3Li6upphw4YZY4wZP368KVy4sPnyyy9t9m3YsKH54IMPTFRUFIPTxCN6O72kzP9vXuDh4aEcOXLI399fy5YtU5YsWVS3bl3rLcJixYpp7dq1Kl68uPLkyaMRI0Y4unS8hKLPx+i7DMHBwZo2bZomTZqkcuXKqWHDhho1apRu3Lihjh07qnr16po6darq1q2rXLlyqVSpUg5+B4hP5ok+FRkzZtSVK1fk7e0t6XFHXIvFovr166tfv34aP368AgMDlTp1arVt25amL6CjNiT9352KP//8U2XKlFH37t01ZMgQRUVFKV26dLp8+bIkqXHjxjpx4oTmzZunffv2qVKlSvrjjz+0bt067dixg98p8Yy2BC+Z6LaF0f9Q8ufPr59//lnDhw+Xl5eXRo8ereXLl0v6v1/OhQoV0vHjx5lVGwnin7+4d+/ereXLl2v27Nlq0KCBDh48qD179sjLy0uTJ0/WN998o/v376tatWrasmWL+vXr58DqkRAsFovmz5+vzJkz6+7duypTpoyWL1+u48ePy8XFxTpZVcaMGeXt7W0d/YcvAACiOTk56dy5c6patarq1KmjIUOGWJdfu3ZNmzZtUt68efXRRx/Jx8dH77//vo4cOaKvv/5aJ06c0K+//qr8+fM7+F28fAgWL5En252vWbNG3333nebMmaPw8HCVLl1avXv3VsqUKTVu3DgtW7ZMkvTWW29pwoQJypkzp5ydnRUZGenAd4CXzfDhw/Xxxx/bdKjLmDGjPvjgA1WqVEkbN25U06ZN9dVXX+n333+Xp6enpkyZopEjRyosLEylSpXivHyJRAeG69eva/PmzRozZoxSpEihZs2aqWzZsmrZsqU1XEjSwYMHlSJFCkVE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cuTIoRYtWmjHjh3KnTu3JGnNmjUqX768teY6dero5MmT1uNkz55dklS8eHFZLBZVrlzZuu6bb75R/vz55eHhoXz58unrr7+2qeG3335TsWLF5OHhoZIlS2rZsmUx7n5s3rxZr7/+utzd3eXn56c+ffrY3DmqXLmyunbtqo8++kjp0qVTQECA2rRpozp16ti81qNHj+Tj46Nvv/32qZ8HACR13LEAgCTC09NTN27csD7fsGGDvL29tW7dOklSaGioAgICVKZMGf3xxx+6evWq2rVrp65du2rmzJmSpC+//FIzZ87U9OnTlT9/fn355ZdaunSpqlSpEus6oqKiVKtWLd29e1ffffedcubMqUOHDsnZ2Vlly5bV2LFjNWDAAB09elSSlDx58qceZ+7cuapWrZqKFy8eY52rq6tcXV2t76tHjx4qUqSI7t27pwEDBujtt9/Wvn375OTkpJ07d+r111/X+vXrVbBgQevdgrlz52rAgAGaMGGCihcvrr1796p9+/by8vJSYGCg7ty5o7p16+qtt97SvHnz9Pfff+ujjz6yqePChQt66623FBQUpNmzZ+vIkSNq3769PDw8bALTrFmz1KlTJ23btk2SdOPGDVWsWFGXLl2Sn5+fJGnFihW6f/++mjVrFuvPGgCSFAMASHQCAwNN/fr1jTHGREVFmXXr1hl3d3fTs2dP6/oMGTKY8PBw6z5Tp041qVOnNvfu3bMuW7lypXFycjKXL182xhjj5+dnRo4caV3/6NEjkzlzZutrGWNM1qxZzZgxY2zqKVq0qBk4cKAxxpi1a9caJycnc/To0afWPmPGDJMyZcr/fI+enp6mW7du/7ndP127ds1IMgcOHDDGGHP69Gkjyezdu9dmu5w5c5p58+bZLPv8889NmTJljDHGTJo0yaRNm9aEhYVZ10+bNs3mWP369TN58+Y1UVFR1m0mTpxokidPbiIjI40xxlSqVMkUL148Rp0FChQwI0aMsD6vW7euCQoKivP7BYCkgqZQAJBIrVixQsmTJ5eHh4dq1aqlZs2a2VwlL1y4sE1b/sOHD6to0aLy8vKyLitXrpyioqJ09OhRhYSE6NKlSypdurR1vYuLi0qWLBmnuvbt26fMmTMrT548z//mpBhNsP7N8ePH9c477yhHjhzy9vZWtmzZJElnz579131CQ0N18uRJtW3bVsmTJ7c+Bg8ebG1GdfToURUpUkQeHh7W/V5//XWb4xw+fFhlypSRxWKxLitXrpzu3bun8+fPW5eVKFEiRg3t2rXTjBkzJElXrlzR6tWr1aZNm1i9ZwBIimgKBQCJ1JtvvqlJkybJzc1NGTNmlIuL7a/sJwNEfHJycorxpf/JEZo8PT3j5XXy5MmjI0eO/Od2devWVdasWTVt2jRlzJhRUVFRKlSokB4+fPiv+0T3K5k2bZpNkJIkZ2dn+wp/iqf9LFq1aqU+ffpo+/bt+u2335Q9e3ZVqFAh3l8bABIL7lgAQCLl5eWlXLlyKUuWLDFCxdPkz59f+/fvV2hoqHXZtm3b5OTkpLx58yplypTy8/PTjh07rOsjIiK0e/dum+OkT59ely5dsj6/c+eOTp8+bX1epEgRnT9/XseOHXtqHW5uboqMjPzPelu0aKH169dr7969MdY9evRIoaGhunHjho4ePar+/furatWqyp8/v27duhXj9STZvGaGDBmUMWNGnTp1Srly5bJ5RHf2zps3rw4cOKDw8HDrfn/88YfNsfPnz6/t27fbBK1t27YpRYoUypw58zPfX9q0adWgQQPNmDFDM2fOVOvWrf/zMwGApIxgAQAviZYtW8rDw0OBgYH666+/tHHjRn3wwQd67733lCFDBknShx9+qOHDh2vZsmU6cuSIOnfurNu3b9scp0qVKpozZ45+/fVXHThwQIGBgTZX+StVqqSKFSuqUaNGWrdunU6fPq3Vq1drzZo1kh6PKnXv3j1t2LBB169f1/37959a70cffaRy5cqpatWqmjhxovbv369Tp05pwYIFeuONN3T8+HGlTp1aadOm1dSpU3XixAn98ssv6tGjh81xfHx85OnpqTVr1ujKlSsKCQmRJAUHB2vYsGH66quvdOzYMR04cEAzZszQ6NGjJT0ONlFRUerQoYMOHz6stWvXatSoUZJkbfrUuXNnnTt3Th988IGOHDmiH3/8UQMHDlSPHj3k5PTff0LbtWunWbNm6fDhwwoMDPzP7QEgSXNwHw8AwFM82Xk7Luv//PNP8+abbxoPDw+TJk0a0759e3P37l3r+kePHpkPP/zQeHt7m1SpUpkePXqYVq1a2RwrJCTENGvWzHh7ext/f38zc+ZMm87bxhhz48YN07p1a5M2bVrj4eFhChUqZFasWGFd37FjR5M2bVojyWa/f3rw4IEZNmyYKVy4sLXmcuXKmZkzZ5pHjx4ZY4xZt26dyZ8/v3F3dzdFihQxmzZtMpLM0qVLrceZNm2a8ff3N05OTqZSpUrW5XPnzjXFihUzbm5uJnXq1KZixYpmyZIl1vXbtm0zRYoUMW5ubqZEiRJm3rx5RpI5cuSIdZtNmzaZUqVKGTc3N+Pr62t69+5trc2Yx523P/zww6e+v6ioKJM1a1bz1ltv/etnAAAvC4sxsew9BwDAS27u3LnWeTjioy/JvXv3lClTJs2YMUMNGzaMhwoBIPGi8zYA4JU1e/Zs5ciRQ5kyZdL+/fvVu3dvNW3a1O5QERUVpevXr+vLL79UqlSpVK9evXiqGAASL4IFAOCVdfnyZQ0YMECXL1+Wn5+fmjRpoiFDhth93LNnzyp79uzKnDmzZs6cGavO9wCQ1NEUCgAAAIDdGBUKAAAAgN0IFgAAAADsRrAAAAAAYDeCBQAAAAC7ESwAAAAA2I1gAQAAAMBuBAsAAAAAdiNYAAAAALAbwQIAAACA3f4fe+PecJK/zIEAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "shipping_return_rate = (\n",
        "    df.groupby('Shipping_Method')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "shipping_return_rate"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 210
        },
        "id": "1Mj8csL5dGNt",
        "outputId": "5bbd0d6e-44b8-43a9-ebc2-49b73f653cd0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Shipping_Method\n",
              "Standard    29.411765\n",
              "Express     29.087569\n",
              "Next-Day    28.503563\n",
              "Name: Return_Status, dtype: float64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Return_Status</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Shipping_Method</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Standard</th>\n",
              "      <td>29.411765</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Express</th>\n",
              "      <td>29.087569</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Next-Day</th>\n",
              "      <td>28.503563</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> float64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(7, 5))\n",
        "\n",
        "shipping_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Shipping Method')\n",
        "plt.xlabel('Shipping Method')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=0)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "btL11NrKdKtz",
        "outputId": "2d6ffb26-7d14-42a1-c35f-efd5889b6569"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 700x500 with 1 Axes>"
            ],
            "image/png": "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N6phw4b25U8//VRbtmyRt7e3JCkuLk6tWrXS22+/XfRVAgAAAH/h9BnZvn376vnnn9eFCxckSZGRkZo4caKSk5O1bds2zZgxQzfffHOxFQoAAABczekgu379elWqVEm33367Fi5cqPfff1+bNm1S06ZNddddd+nw4cOaPXt2cdYKAAAA2Dk9tcDNzU1Dhw5Vt27d1K9fP/n4+Gjq1KkKDQ0tzvoAAACAXBX6Yq/IyEh988036tKli1q0aKFp06YVR10AAABAvpwOsikpKXrxxRd13333acSIEerSpYvWr1+vDRs26M4779S2bduKs04AAADAgdNBNjY2VuvXr1fHjh2VnJysfv36qUKFCkpMTNRrr72mhx56SEOHDi3OWgEAAAA7p+fIfvfdd9q0aZOqV6+u3r17q3r16vZ1bdu21c8//6xx48YVS5EAAADAXzl9RrZGjRqaOXOmfv31V73zzjsKDw93WO/l5aXXX3+9yAsEAAAAcuN0kH3//ff13XffqX79+po9e7ZmzJhRnHUBAAAA+XJ6akG9evW0cePG4qwFAAAAcJpTZ2SNMcVdBwAAAFAoTgXZW2+9VZ988okyMzPz7bd7927169dP48ePL5LiAAAAgLw4NbXg7bff1tChQ9W/f3+1a9dODRs2VGhoqLy8vPTHH39ox44d+vHHH/XLL79o4MCB6tevX3HXDQAAgH84p4Js27ZttXHjRv3444/69NNPlZSUpAMHDujixYuqWLGi6tevryeeeEI9evRQQEBAcdcMAAAAOH+xlyQ1b95czZs3L65aAAAAAKc5ffstAAAAoCQhyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEu6piC7d+9ejRgxQo888ohOnDghSVq8eLF++eWXIi0OAAAAyEuhg+zKlStVp04drV+/Xp9//rnOnTsnSdqyZYtGjx5d5AUCAAAAuSl0kB02bJheffVVLV26VB4eHvb2Nm3aaN26dUVaHAAAAJCXQgfZbdu2qUuXLjnag4KCdOrUqSIpCgAAAChIoYNsuXLldPTo0RztmzZt0k033VQkRQEAAAAFKXSQffjhhzV06FAdO3ZMNptN2dnZWr16tYYMGaInnniiOGoEAAAAcih0kH399ddVs2ZNhYWF6dy5c6pdu7ZatGihpk2basSIEcVRIwAAAJBD6cJu4OHhoffee0+jRo3Stm3bdO7cOdWvX181atQojvoAAACAXBX6jOy4ceN04cIFhYWF6Z577lH37t1Vo0YNXbx4UePGjSuOGgEAAIAcCh1kx44da7937NUuXLigsWPHFklRAAAAQEEKHWSNMbLZbDnat2zZovLlyxdJUQAAAEBBnJ4jGxAQIJvNJpvNpptvvtkhzGZlZencuXPq27dvsRQJAAAA/JXTQXby5MkyxqhXr14aO3as/P397es8PDwUERGhJk2aFEuRAAAAwF85HWRjY2MlSVWrVlXTpk3l7u5ebEUBAAAABSn07bdatmxp/zk9PV2ZmZkO6/38/P5+VQAAAEABCn2x14ULFzRw4EAFBQXJx8dHAQEBDg8AAADgeih0kH3hhRf03XffacaMGfL09NR//vMfjR07VqGhoZo1a1Zx1AgAAADkUOipBQsXLtSsWbPUqlUr9ezZU3fddZeqV6+u8PBwJSUlqUePHsVRJwAAAOCg0Gdkz5w5o8jISEl/zoc9c+aMJKl58+ZatWpV0VYHAAAA5KHQQTYyMlL79u2TJNWsWVOfffaZpD/P1JYrV65IiwMAAADyUugg27NnT23ZskWSNGzYME2bNk1eXl4aNGiQXnjhhSIvEAAAAMhNoefIDho0yP5zdHS0du3apZ9++knVq1dXVFRUkRYHAAAA5KXQQfavwsPDFR4eLkmaO3euHnzwwb9dFAAAAFCQQk0tuHz5srZv365ff/3Vof2LL75Q3bp1uWMBAAAArhung+z27dtVvXp11a1bV7Vq1dIDDzyg48ePq2XLlurVq5c6dOigvXv3FmetAAAAgJ3TUwuGDh2q6tWra+rUqfr444/18ccfa+fOnXryySe1ZMkSeXt7F2edAAAAgAOng+yGDRv07bffql69errrrrv08ccf66WXXtLjjz9enPUBAAAAuXJ6asGpU6cUGhoqSfL395ePj4/uvPPOv7XzVatW6b777lNoaKhsNpsWLFjgsD4uLk42m83h0b59+7+1TwAAANwYnD4ja7PZdPbsWXl5eckYI5vNposXLyotLc2hn5+fn9M7P3/+vOrWratevXrpgQceyLVP+/btlZCQYF/29PR0enwAAADcuJwOssYY3XzzzQ7L9evXd1i22WzKyspyeucdOnRQhw4d8u3j6empkJAQp8cEAADAP4PTQfb7778vzjrytGLFCgUFBSkgIEBt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7Nnq1avXtb40yANBFpKk06dPq02bNvroo4+0detW7du3T3PmzNGECRPUqVMnSX9eIb18+XIdO3bM/oatUaOGPv/8c23evFlbtmzRo48+WqgzrZL06KOPymazqXfv3tqxY4e+/vpr/fvf/3boU6NGDW3cuFHffPONfv31V40cOVIbNmwokrGB4pKRkaFjx445PE6dOqWsrCw99thjiomJUc+ePZWQkKCtW7dq4sSJDtsfPHhQgwcPVnJysj7++GO9/fbbeu655/Ld59ChQ7VmzRoNHDhQmzdv1u7du/XFF1/Y/7AvWrRIb731ljZv3qwDBw5o1qxZys7O1i233KL169fr9ddf18aNG3Xw4EF9/vnnOnnypGrVqlVsrxFwtTp16qhHjx5666237G0FHdNnz57V448/rmeffVYdOnRQUlKSPv30U82dO9c+RkREhFatWqXff/9dp06dyrcGY4yOHTumo0ePaufOnXr//ffVtGlT+fv72+93GxAQoAoVKmjmzJnas2ePvvvuOw0ePDjX8Z566imNHz9exhh16dLl775E+CsXz9FFCZGenm6GDRtmbr/9duPv72/KlCljbrnlFjNixAhz4cIFY4wxX375palevbopXbq0CQ8PN8YYs2/fPtO6dWvj7e1twsLCzNSpU03Lli3Nc889Zx87t0n2devWNaNHj7Yvr1271tStW9d4eHiYevXqmXnz5jlckJWenm7i4uKMv7+/KVeunOnXr58ZNmyYqVu3rn2MvK4SL2hsoDjExsYaSTket9xyixk7dqypVKmSOXXqlL3/vHnzjIeHh9m8ebMx5s+Lvfr372/69u1r/Pz8TEBAgHnppZccLv7K6wKW//3vf6Zdu3bG19fX+Pj4mKioKPvFLz/88INp2bKlCQgIMN7e3iYqKsp+McqOHTtMTEyMCQwMNJ6enubmm292uHATKGq5/X973759xsPDw1wdUfI7pnv27Gnq1KnjcHeAiRMnmvLly5vDhw8bY/78OxAVFWU8PT1NftEnISHB/l612WzG39/fNGrUyIwbN86kpqY69F26dKmpVauW8fT0NFFRUWbFihW5XhR99uxZU6ZMGdO/f/9reYlQAJsxV92UEABQIrRq1Ur16tVz6tuIAJRc+/fvV7Vq1bRhwwbdfvvtri7nhsPFXgAAAEXs0qVLOn36tEaMGKE777yTEFtM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SUlJ+uWXXxQZGensywTgH4gzsgBuOL6+vmrcuLEmTZqkFi1a6LbbbtPIkSPVu3dvTZ069W+NXaZMGQ0dOlSPPvqomjVrJl9fX3366acOfapXr64HHnhA99xzj+6++25FRUX9rSvw3dzctGDBAp07d0533HGHnnrqKftdC7y8vJwex8/PT35+fnmuf+WVVzRy5EjFx8erVq1aat++vb766itVrVpVknTTTTdp7NixGjZsmIKDg+1TFQpis9n0xRdfKCAgQC1atFB0dLQiIyMdXreHHnpII0eO1IsvvqgGDRrowIED6tevn9PPDcA/k80YY1xdBABYQWJiop5//vl8v9lqzJgxWrBggTZv3lystaxevVrNmzfXnj17VK1atWLdFwCUVEwtAAALmD9/vnx9fVWjRg3t2bNHzz33nJo1a0aIBfCPRpAFAAs4e/ashg4dqoMHD6pixYqKjo7WxIkTXV0WALgUUwsAAABgSVzsBQAAAEsiyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEsiyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEv6/wA74V752D4ZzQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "payment_return_rate = (\n",
        "    df.groupby('Payment_Method')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(payment_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kv1-H3mBdMde",
        "outputId": "13b7d186-f92d-4dfe-fd05-cda8967aaf31"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Payment_Method\n",
            "Credit Card    31.012146\n",
            "COD            30.502885\n",
            "Debit Card     27.486296\n",
            "Wallet         27.137255\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "payment_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Payment Method')\n",
        "plt.xlabel('Payment Method')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "kQh_4PfIdRpT",
        "outputId": "e49fdfe2-eae1-4690-fd0e-da1c9921eb01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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zp8/r9q1a6t9+/aaMGGCbG1tzaMf+vTpo379+hEqkoMBWFlMTIxhGIaxbds2w87OzmjatKlx6dKleNd99OjRyywNr5EjR44YFStWNPLly2e4ubkZzs7OxnvvvWcsW7bMvE7RokWNfPnyGdu3bzcMwzCGDh1qZMqUyTh69Ki1ygaSRez7smEYxrlz54whQ4YYjo6OxoABA+Jd/9GjR8b9+/dfVnl4zR07dsxwdnY2GjduHKd9zZo1Rvny5Y3du3cb2bJlMz766CMjKirKMAzD2L59u9GxY0fj/Pnz1ij5tUGPBV464/9H34WHhys0NNT8zW+5cuW0atUqLViwQEOHDlVISIh5m9iLkMV2dwJJ6ejRoypfvrxKliypadOmad++fRo2bJiOHj2qbt26ad68eZIeD81zcXFRly5d1KZNG3311VdavXq1ChYsaOVHACSN2PfnR48eSZKio6Pl5+enDh06qHfv3lq4cKFGjhxpXj/2att2dnZycnJ6+QXjtZQlSxb99NNP2rNnj5o1a2Zuz5gxo8LDw1WzZk3VqFFDU6dONQ9/mj9/vkJCQsy9bkgm1k42eL3Efgu2YsUKo0qVKkbBggUNf39/488//zTu3btnGIZhrF271rC1tTU6der0zJ4LIKmEhYUZ1apVM7p37/7UspUrVxqlS5c2ChYsaOzcudPcXrBgQcNkMhkHDhx4iZUCySv2/XndunVG69atjQYNGhgDBgwwbt26ZRjG456LQYMGGfnz5zdGjhxpzVLxmho7dqyxbds2wzAM4+7du8a8efOMrFmzGk2bNjWvM2bMGMNkMhkjR440Dh8+bJw8edLo1auXkS5dOuPIkSPWKv21QY8FXiqTyaTffvtNzZo1U7ly5TRlyhRdv35dvXr10vLlyxUREaGaNWtqzZo1mjZtmnmCFZBc7t69q+vXr6t+/fqSHveOxb7m/P391adPH50/f147duwwb3P06FGdO3dORYsWtUbJQLIwmUxaunSpGjRooHTp0il79uzasmWL3n33Xd28eVN+fn5q166dmjZtqu+++47rt+ClioiI0IYNG1SjRg3t3btXadKkUb169TR27Fht3bpVTZo0kST17t1b/fr1088//6yyZcvqgw8+0KpVq7Rx40YVKlTIyo/i1cdZoZBsjHiuZHnmzBk1adJELVu21CeffKJ79+6pYMGCevjwodzc3DRixAjVq1dPLi4u2rRpk7y8vFSgQAErPQK8Dg4cOKCSJUtqzZo1ql69urn9ydfvO++8o8jISK1Zs0YPHz7kisJ4JR0+fFgffPCBevTooY8++kgXLlxQmTJldP/+fWXNmlWbNm1ShgwZdObMGf36669q0qSJcuXKZe2y8Rq5evWqevTooRUrVmjDhg0qWbKkwsPDtWLFCvXu3VtlypTRggULJD0+Q9T169eVLl06Zc6cWZkyZbJy9a8HeiyQLGLP93/37l39888/unLliqTH43BbtGih1q1bKyQkREWKFFH9+vV1+fJlOTo6asyYMfrll18UERGhKlWqECqQLK5fv669e/dq3759ypkzp+zt7bV7925J/5vP82Qotre3l7OzsyQRKpDqxb7GHz58GOf6Kzdu3FD58uXNoaJatWqqU6eO5s6dq+vXr+vdd9/VjRs3lDNnTvXu3ZtQgZfOy8tL48aNk7+/v6pXr649e/bE6bnYuXOnueeiYMGCqly5st58801CxUtEsECSi71C8V9//aXWrVvrww8/1OLFixUZGSlfX181bNhQadOm1ciRI/XWW29p1KhRMplMKlGihIKDg/Xzzz+bTx0HJLVjx46pQYMGGjhwoEaOHCkPDw+1aNFCo0aN0u7du2VjY2MeChUdHa2YmBjZ2tqqWLFiksQVWpGqxb4/nzx5UgEBAWrSpIl++uknSVK1atXUq1cvSVKvXr1UunRp/fTTT6pVq5by5Mmj7du3q169eua/CeBlig3EXl5e+u6771SnTh1Vr15du3fvNoeLr7/+Wvv27VOdOnWsXO3ri2CBJBX7n1ZwcLAqV66s/Pnzmy9U4+joKJPJZD7HeUhIiLy9veXi4iJJSps2rZYtW6bZs2dz1gYki9izP1WuXFnTpk3T/PnzJUkfffSR8ubNq7fffltr167VgwcPJD3+Rnf48OHatGmTmjdvLklcoRWpVuz78+HDh1W1alW5urqqffv2atGihXmd/Pnz6+bNmzpx4oTq1asn6fHfQZ48eRQUFKRFixbJxsaGvwO8NLFf5tjY/O8jq7e3t8aPHy9/f3/VqFHDHC7q1q2rIUOG6OLFi/rnn3+sVfJrjTkWSHIhISGqXr26atSooe+//97cHvufmvT4m+APPvhA58+fV6tWrXTixAnNmTNHwcHBXL0YyeLWrVt699139dZb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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "gender_return_rate = (\n",
        "    df.groupby('User_Gender')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(gender_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IrjESkg3dThc",
        "outputId": "acfa53f8-d56a-401d-bffe-ac902485cb2c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "User_Gender\n",
            "Female    30.201863\n",
            "Male      27.722772\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(6, 5))\n",
        "\n",
        "gender_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Gender')\n",
        "plt.xlabel('Gender')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=0)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "st6jy0cSdYKK",
        "outputId": "442fcac1-32a5-43c0-95fc-e4e3d2363f36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk4AAAHqCAYAAADyPMGQAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAOaFJREFUeJzt3Xt8z/X///H72w7vzWZjs4MxmzkkoRxyPuU0S4rQR4kN+Tp/igglNfWhw+cTFR+lAx8ipXR0LCGEIuRQi+VY5pjNNhvbXr8/unj/erfhObbeb3a7Xi6vS+/X8/l8vV6P1zveu3u9nnu9bZZlWQIAAMAVlXJ1AQAAANcLghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAXEJCQoL8/f1dXYZLzZkzRzabTQcOHHB1KYBbIDgBLnTxh9LFxdPTUxUrVlRCQoJ+/fXXq9rnnj179PTTT7vtD7ro6Ginc/bz81OjRo00d+7cq97n0qVL9fTTTxddkS6Ql5enuXPnqkOHDipfvry8vLwUGhqqjh07atasWcrOznZ1iQAkebq6AADSpEmTVKVKFWVlZWnTpk2aM2eO1q9fr127dsnHx6dQ+9qzZ48SExPVpk0bRUdHF0/B1+i2227To48+Kkk6evSo3nzzTcXHxys7O1sDBw4s9P6WLl2qGTNmXLfh6dy5c+rWrZtWrFihZs2aafTo0QoLC9Pp06e1du1aDR06VJs3b9Zbb73l6lKBEo/gBLiBuLg4NWzYUJL00EMPqXz58nr++ef16aef6r777nNxdX/IyMiQn59fkeyrYsWKevDBBx3rCQkJiomJ0dSpU68qOF3vRo4cqRUrVmjatGl6+OGHnfoeffRR7d27V1988YWLqitaRfnnCHAFbtUBbqhly5aSpOTkZKf2n376ST169FBQUJB8fHzUsGFDffrpp47+OXPmqGfPnpKkO+64w3E7bM2aNZIkm81W4FWZ6OhoJSQkOO3HZrM5rnaEhoaqUqVKkqQ2bdqodu3a2rNnj+644w6VLl1aFStW1AsvvHDV5xsSEqKaNWvmO99169apZ8+eqly5sux2uyIjIzVy5EidO3fOMSYhIUEzZsxwnN/F5aK8vDxNmzZNt9xyi3x8fBQWFqZBgwbp999/N67vl19+UWxsrPz8/BQREaFJkybJsixJkmVZio6O1j333JNvu6ysLAUGBmrQoEGX3Pfhw4f15ptvqlOnTvlC00XVq1fX0KFDndpMzys6Olp33XWX1q9fr0aNGsnHx0cxMTEF3hrdvXu32rZtK19fX1WqVEnPPvus8vLyCqxp2bJlatmypfz8/FSmTBl17txZu3fvdhpzcY5YcnKy7rzzTpUpU0a9e/e+5HsBXA+44gS4oYvzk8qVK+do2717t5o3b66KFStq3Lhx8vPz0/vvv6+uXbvqww8/VLdu3dSqVSv985//1CuvvKLHH39cN998syQ5/ltYQ4cOVUhIiCZOnKiMjAxH+++//65OnTrp3nvv1X333acPPvhAY8eOVZ06dRQXF1fo4+Tk5OjIkSNO5ytJixYtUmZmpoYMGaLg4GB9++23evXVV3XkyBEtWrRIkjRo0CD99ttv+uKLLzRv3rx8+x40aJDmzJmjfv366Z///Kf279+v6dOna9u2bdqwYYO8vLwuW1tubq46deqkJk2a6IUXXtDy5cv11FNPKScnR5MmTZLNZtODDz6oF154QadPn1ZQUJBj288++0xpaWlOV9f+atmyZcrNzb3smIIU5rz27dunHj16aMCAAYqPj9fbb7+thIQENWjQQLfccoskKSUlRXfccYdycnIcf75mzZolX1/ffMeeN2+e4uPjFRsbq+eff16ZmZmaOXOmWrRooW3btjndIs7JyVFsbKxatGihf//73ypdunShzhNwOxYAl5k9e7Ylyfryyy+tEydOWIcPH7Y++OADKyQkxLLb7dbhw4cdY9u1a2fVqVPHysrKcrTl5eVZzZo1s6pXr+5oW7RokSXJWr16db7jSbKeeuqpfO1RUVFWfHx8vrpatGhh5eTkOI1t3bq1JcmaO3euoy07O9sKDw+3unfvfsVzjoqKsjp27GidOHHCOnHihLVz506rT58+liRr2LBhTmMzMzPzbT9lyhTLZrNZBw8edLQNGzbMKujjbN26dZYka/78+U7ty5cvL7D9r+Lj4y1J1ogRIxxteXl5VufOnS1vb2/rxIkTlmVZVlJSkiXJmjlzptP2d999txUdHW3l5eVd8hgjR460JFnbt293as/Ozna8RydOnLBOnjx5VecVFRVlSbK+/vprR9vx48ctu91uPfroo462Rx55xJJkbd682WlcYGCgJcnav3+/ZVmWdfbs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IR8fH/3+++/as2eP1q9fr927d2v48OEaMmRIcdcNAADwtzMKTu3atdOWLVu0fv16vffee5o/f74OHjyoc+fOqXz58qpXr5769u2r3r17q1y5csVdMwAAgEsYTw6XpBYtWqhFixbFVQsAAIBbK/R31QEAAJRUBCcAAABDBCcAAABDBCcAAABDBCcAAABDVxWckpOTNWHCBN1///06fvy4JGnZsmXavXt3kRYHAADgTgodnNauXas6depo8+bNWrx4sdLT0yVJO3bs0FNPPVXkBQIAALiLQgencePG6dlnn9UXX3whb29vR3vbtm21adOmIi0OAADAnRQ6OO3cuVPdunXL1x4aGqqTJ08WSVEAAADuqNDBqWzZsjp69Gi+9m3btqlixYpFUhQAAIA7KnRw6tWrl8aOHauUlBTZbDbl5eVpw4YNGj16tPr27VscNQIAALiFQgenyZMnq2bNmoqMjFR6erpq1aqlVq1aqVmzZpowYUJx1AgAAOAWCvUlv5Lk7e2tN954QxMnTtTOnTuVnp6uevXqqXr16sVRHwAAgNso9BWnSZMmKTMzU5GRkbrzzjt13333qXr16jp37pwmTZpUHDUCAAC4hUIHp8TERMezm/4sMzNTiYmJRVIUAACAOyp0cLIsSzabLV/7jh07FBQUVCRFAQAAuCPjOU7lypWTzWaTzWZTjRo1nMJTbm6u0tPTNXjw4GIpEgAAwB0YB6dp06bJsiz1799fiYmJCgwMdPR5e3srOjpaTZs2LZYiAQAA3IFxcIqPj5ckValSRc2aNZOXl1exFQUAAOCOCv04gtatWzteZ2Vl6fz58079AQEB114VAACAGyr05PDMzEwNHz5coaGh8vPzU7ly5ZwWAACAG1Whg9OYMWP01VdfaebMmbLb7XrzzTeVmJioiIgIzZ07tzhqBAAAcAuFvlX32Wefae7cuWrTpo369eunli1bqlq1aoqKitL8+fPVu3fv4qgTAADA5Qp9xen06dOKiYmR9Md8ptOnT0uSWrRooa+//rpoqwMAAHAjhQ5OMTEx2r9/vySpZs2aev/99yX9cSWqbNmyRVocAACAOyl0cOrXr5927NghSRo3bpxmzJghHx8fjRw5UmPGjCnyAgEAANxFoec4jRw50vG6ffv2+umnn7R161ZVq1ZNdevWLdLiAAAA3Emhg9NfRUVFKSoqSpL0wQcfqEePHtdcFAAAgDsq1K26nJwc7dq1Sz///LNT+yeffKJbb72V36gDAAA3NOPgtGvXLlWrVk233nqrbr75Zt177706duyYWrdurf79+ysuLk7JycnFWSsAAIBLGd+qGzt2rKpVq6bp06fr3Xff1bvvvqsff/xRAwYM0PLly+Xr61ucdQIAALiccXD67rvvtHLlSt12221q2bKl3n33XT3++OPq06dPcdYHAADgNoxv1Z08eVIRERGSpMDAQPn5+alJkybFVhgAAIC7Mb7iZLPZdPbsWfn4+MiyLNlsNp07d05paWlO4wICAoq8SAAAAHdgHJwsy1KNGjWc1uvVq+e0brPZlJubW7QVAgAAuAnj4LR69erirAMAAMDtGQen1q1bF2cdAAAAbq/Q31VXlL7++mt16dJFERERstls+vjjj536ExISZLPZnJZOnTq5plgAAFDiuTQ4ZWRk6NZbb9WMGTMuOaZTp046evSoY3n33Xf/xgoBAAD+v2v+rrprERcXp7i4uMuOsdvtCg8P/5sqAgAAuDSXXnEysWbNGoWGhuqmm27SkCFDdOrUqcuOz87OVlpamtMCAABQFNw6OHXq1Elz587VqlWr9Pzzz2vt2rWKi4u77CMPpkyZosDAQMcSGRn5N1YMAABuZIW+VZeRkaHnnntOq1at0vHjx5WXl+fU/8svvxRZcb169XK8rlOnjurWrauqVatqzZo1ateuXYHbjB8/XqNGjXKsp6WlEZ4AAECRKHRweuihh7R27Vr16dNHFSpUkM1mK466ChQTE6Py5ctr3759lwxOdrtddrv9b6sJAACUHIUOTsuWLdOSJUvUvHnz4qjnso4cOaJTp06pQoUKf/uxAQAACh2cypUrp6CgoCI5eHp6uvbt2+dY379/v7Zv366goCAFBQUpMTFR3bt3V3h4uJKTk/XYY4+pWrVqio2NLZLjAwAAFEahJ4c/88wzmjhxojIzM6/54Fu2bFG9evUc33k3atQo1atXTxMnTpSHh4d++OEH3X333apRo4YGDBigBg0aaN26ddyKAwAALlHoK07/+c9/lJycrLCwMEVHR8vLy8up//vvvzfeV5s2bWRZ1iX7V6xYUdjyAAAAik2hg1PXrl2LoQwAAAD3V6jglJOTI5vNpv79+6tSpUrFVRMAAIBbKtQcJ09PT7344ovKyckprnoAAADcVqEnh7dt21Zr164tjloAAADcWqHnOMXFxWncuHHauXOnGjRoID8/P6f+u+++u8iKAwAAcCeFDk5Dhw6VJL300kv5+mw222W/Rw4AAOB6Vujg9NfvpgMAACgpCj3HCQAAoKQq9BWnSZMmXbZ/4sSJV10MAACAOyt0cProo4+c1i9cuKD9+/fL09NTVatWJTgBAIAbVqGD07Zt2/K1paWlKSEhQd26dSuSogAAANxRkcxxCggIUGJiop588smi2B0AAIBbKrLJ4ampqUpNTS2q3QEAALidQt+qe+WVV5zWLcvS0aNHNW/ePMXFxRVZYQAAAO6m0MFp6tSpTuulSpVSSEiI4uPjNX78+CIrDAAAwN0UOjjt37+/OOoAAABwe4We49S/f3+dPXs2X3tGRob69+9fJEUBAAC4o0IHp//97386d+5cvvZz585p7ty5RVIUAACAOzK+VZeWlibLsmRZls6ePSsfHx9HX25urpYuXarQ0NBiKRIAAMAdGAensmXLymazyWazqUaNGvn6bTabEhMTi7Q4AAAAd2IcnFavXi3LstS2bVt9+OGHCgoKcvR5e3srKipKERERxVIkAACAOzAOTq1bt5b0x2/VVa5cWTabrdiKAgAAcEeFnhweFRWl9evX68EHH1SzZs3066+/SpLmzZun9evXF3mBAAAA7qLQwenDDz9UbGysfH199f333ys7O1vSH1+5Mnny5CIvEAAAwF0UOjg9++yzeu211/TGG2/Iy8vL0d68eXN9//33RVocAACAOyl0cEpKSlKrVq3ytQcGBurMmTNFURMAAIBbKnRwCg8P1759+/K1r1+/XjExMUVSFAAAgDsqdHAaOHCgHn74YW3evFk2m02//fab5s+fr9GjR2vIkCHFUSMAAIBbKPSX/I4bN055eXlq166dMjMz1apVK9ntdo0ePVojRowojhoBAADcQqGDk81m0xNPPKExY8Zo3759Sk9PV61ateTv769z587J19e3OOoEAABwuULfqrvI29tbtWrVUqNGjeTl5aWXXnpJVapUKcraAAAA3IpxcMrOztb48ePVsGFDNWvWTB9//LEkafbs2apSpYqmTp2qkSNHFledAAAALmd8q27ixIl6/fXX1b59e33zzTfq2bOn+vXrp02bNumll15Sz5495eHhUZy1AgAAuJRxcFq0aJHmzp2ru+++W7t27VLdunWVk5OjHTt28L11AACgRDC+VXfkyBE1aNBAklS7dm3Z7XaNHDmS0AQAAEoM4+CUm5srb29vx7qnp6f8/f2LpSgAAAB3ZHyrzrIsJSQkyG63S5KysrI0ePBg+fn5OY1bvHhx0VYIAADgJoyDU3x8vNP6gw8+WOTFAAAAuDPj4DR79uzirAMAAMDtXfUDMAEAAEoaghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhghMAAIAhlwanr7/+Wl26dFFERIRsNps+/vhjp37LsjRx4kRVqFBBvr6+at++vfbu3euaYgEAQInn0uCUkZGhW2+9VTNmzCiw/4UXXtArr7yi1157TZs3b5afn59iY2OVlZX1N1cKAAAgebry4HFxcYqLiyuwz7IsTZs2TRMmTNA999wjSZo7d67CwsL08ccfq1evXn9nqQAAAO47x2n//v1KSUlR+/btHW2BgYFq3LixNm7ceMntsrOzlZaW5rQAAAAUBbcNTikpKZKksLAwp/awsDBHX0GmTJmiwMBAxxIZGVmsdQIAgJLDbYPT1Ro/frxSU1Mdy+HDh11dEgAAuEG4bXAKDw+XJB07dsyp/dixY46+gtjtdgUEBDgtAAAARcFtg1OVKlUUHh6uVatWOdrS0tK0efNmNW3a1IWVAQCAksqlv1WXnp6uffv2Odb379+v7du3KygoSJUrV9YjjzyiZ599VtWrV1eVKlX05JNPKiIiQl27dnVd0QAAoMRyaXDasmWL7rjjDsf6qFGjJEnx8fGaM2eOHnvsMWVkZOj//u//dObMGbVo0ULLly+Xj4+Pq0oGAAAlmEuDU5s2bWRZ1iX7bTabJk2apEmTJv2NVQEAABTMbec4AQAAuBuCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCGCEwAAgCG3Dk5PP/20bDab01KzZk1XlwUAAEooT1cXcCW33HKLvvzyS8e6p6fblwwAAG5Qbp9CPD09FR4e7uoyAAAA3PtWnSTt3btXERERiomJUe/evXXo0CFXlwQAAEoot77i1LhxY82ZM0c33XSTjh49qsTERLVs2VK7du1SmTJlCtwmOztb2dnZjvW0tLS/q1wAAHCDc+vgFBcX53hdt25dNW7cWFFRUXr//fc1YMCAAreZMmWKEhMT/64SAQBACeL2t+r+rGzZsqpRo4b27dt3yTHjx49XamqqYzl8+PDfWCEAALiRXVfBKT09XcnJyapQocIlx9jtdgUEBDgtAAAARcGtg9Po0aO1du1aHThwQN988426desmDw8P3X///a4uDQAAlEBuPcfpyJEjuv/++3Xq1CmFhISoRYsW2rRpk0JCQlxdGgAAKIHcOjgtXLjQ1SUAAAA4uPWtOgAAAHdCcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADBEcAIAADB0XQSnGTNmKDo6Wj4+PmrcuLG+/fZbV5cEAABKILcPTu+9955GjRqlp556St9//71uvfVWxcbG6vjx464uDQAAlDBuH5xeeuklDRw4UP369VOtWrX02muvqXTp0nr77bddXRoAAChh3Do4nT9/Xlu3blX79u0dbaVKlVL79u21ceNGF1YG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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Age_Group'] = pd.cut(\n",
        "    df['User_Age'],\n",
        "    bins=[0, 24, 34, 44, 54, 100],\n",
        "    labels=['Under 25', '25-34', '35-44', '45-54', '55+']\n",
        ")\n",
        "\n",
        "df[['User_Age', 'Age_Group']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "vNDVO59Cdaw_",
        "outputId": "51e8cef4-7a0f-4d39-a427-0a2bc7b1f277"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   User_Age Age_Group\n",
              "0        57       55+\n",
              "1        55       55+\n",
              "2        37     35-44\n",
              "3        47     45-54\n",
              "4        35     35-44"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0392c70a-39af-460e-a5be-436ab3385f2e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>User_Age</th>\n",
              "      <th>Age_Group</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>57</td>\n",
              "      <td>55+</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>55</td>\n",
              "      <td>55+</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>37</td>\n",
              "      <td>35-44</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>47</td>\n",
              "      <td>45-54</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>35</td>\n",
              "      <td>35-44</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0392c70a-39af-460e-a5be-436ab3385f2e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-0392c70a-39af-460e-a5be-436ab3385f2e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-0392c70a-39af-460e-a5be-436ab3385f2e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df[['User_Age', 'Age_Group']]\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"User_Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 10,\n        \"min\": 35,\n        \"max\": 57,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          55,\n          35,\n          37\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Age_Group\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"55+\",\n          \"35-44\",\n          \"45-54\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age_return_rate = (\n",
        "    df.groupby('Age_Group', observed=True)['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(age_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uyXCb0bUdgIE",
        "outputId": "572f2cb9-e766-45e2-ea2f-363e02f929d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Age_Group\n",
            "25-34       29.482072\n",
            "35-44       29.305423\n",
            "Under 25    28.954424\n",
            "55+         28.867761\n",
            "45-54       28.406910\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "age_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Age Group')\n",
        "plt.xlabel('Age Group')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=0)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "gxWYNVJzdiM4",
        "outputId": "c7fefdd8-4310-4c4e-eeab-02716df6b4cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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jIxUYGCg3Nzc9Pfffys8PNz6M8lOenq6vLy8bI4k3MjT0zNH9eZE165dNXToUMXGxmr06NH66quv1LhxY9WoUeOWy16vr3nz5pnO//PPPzN8gb4VM/tetWpVOTo6ateuXRnmBQcHS5IcHTP/aM5qzOREVkd2shqfAHA7CBYA7hkODg6Kjo7Wgw8+qMmTJ2vkyJHWL5VOTk7WL+RZye60m1KlSuncuXM2bVeuXNGxY8dM121Ghw4dFBwcrDfffFP9+vWTm5ubdu7cqb1792rmzJnq2bOnte/PP/+cYfms9rlKlSpasWKFmjdvfttfeNPT0/Xnn39a/xIuSXv37pUkm7swlS5dWh06dFBsbKy6d++uX3/9VZMmTbrl+g8cOKD169crIiLC+qX9xm0/99xzmj17tsaMGSN/f39Jsjmqcd3NbWb23c3NTSEhIYqLi9Pff/9t+kiYv7+/duzYofT0dJujFn/88Yd1vvT/b1Zw8xjN6ohGTt8bALgR11gAuKeEhISoSZMmmjRpki5fviwvLy+FhITok08+yTQEnDp1yvrv6889uPnLmfTvl821a9fatH366acF4i/CkZGROn36tD777DNJ//+oyI1HQQzD0AcffJBh2az2+emnn1ZaWppef/31DMtcu3Yt059RZiZPnmxTw+TJk+Xk5KTWrVvb9Hvuuee0Z88evfLKK3JwcFDXrl1vue7rRxRGjBihzp0727yefvppBQcHW/v4+vqqdu3amjVrls1pSnFxcdq5c2ee7vvYsWOVlpamHj16ZHpKVE6PTknSo48+quPHj2vu3Lk2NXz00Udyd3e3Bip/f385ODhkGKMff/xxluvO6XsDANdxxALAPeeVV15Rly5dFBMTo/79+2vKlClq0aKF6tSpo759+yogIEAnTpzQhg0bdOTIEcXHx0v696nWDg4Oevvtt5WUlCQXFxc99NBD8vLyUp8+fdS/f3+Fhobq4YcfVnx8vJYvX66yZcvaeW//fUhg7dq19f7772vgwIEKDAxUlSpVNHz4cP39998qUaKEvv3220yfwdCoUSNJ0uDBg9W2bVvrl/rg4GD169dP0dHR2r59ux555BE5OTlp3759mjdvnj744AN17tw527pcXV21bNkyhYWFqWnTplq6dKl+/PFHjR49OsPpRB06dFCZMmU0b948tW/fPsvrG24UGxur+vXry8/PL9P5TzzxhAYNGqStW7eqYcOGevPNN/Xkk0+qefPm6tWrl86ePavJkyerdu3aNgHA7L63bNlSkydP1qBBg1StWjXrk7evXLmivXv3KjY2Vs7OzvLx8bnlPr7wwgv65JNPFB4eri1btqhSpUqaP3++9ajO9Ws6PDw81KVLF3300UeyWCyqUqWKfvjhhyyvB8nNewMAVva7IRUA5J/rt3X9/fffM8xLS0szqlSpYlSpUsV6y9fExESjZ8+eho+Pj+Hk5GSUL1/eeOyxx4z58+fbLPvZZ58ZAQEBhoODg83tO9PS0ozIyEijbNmyRrFixYy2bdsa+/fvz/J2s5nVFRwcbNx3330Z2sPCwmxud5oVf39/o0OHDpnOi4mJsbmt6J49e4w2bdoY7u7uRtmyZY2+fftab4V6461Hr127ZgwaNMjw9PQ0LBZLhlvPfvrpp0ajRo2MokWLGsWLFzfq1KljjBgxwjh69Gi2tYaFhRlubm5GYmKi8cgjjxjFihUzvL29jXHjxhlpaWmZLvPiiy8akozZs2ff8mexZcsWQ5Lx6quvZtnn4MGDhiRj6NCh1rY5c+YYgYGBhouLi1G7dm1j8eLFRmhoqBEYGJhh+dvd9+u2bdtm9OzZ06hYsaLh7OxsuLm5GXXr1jVefvllY//+/TZ9sxobhmEYJ06cMHr16mWULVvWcHZ2NurUqWPzHl536tQpIzQ01ChWrJhRqlQpo1+/fsauXbsyvd1sbt8bADAMw7AYBo/RBAAUfEOHDtX06dN1/PhxFStW7I5tt379+vL09Mz0GpS7UXh4uObPn5/paVoAkB2usQAAFHiXL1/WV199pdDQ0HwLFVevXtW1a9ds2tasWaP4+HiFhITkyzYB4G7CNRYAgALr5MmTWrFihebPn6/Tp0/rpZdeyrdt/f3332rTpo169OghX19f/fHHH5o2bZp8fHzUv3//fNsuANwtCBYAgAJrz5496t69u7y8vPThhx+qfv36+batUqVKqVGjRvr888916tQpubm5qUOHDnrrrbdUpkyZfNsuANwtuMYCAAAAgGlcYwEAAADANIIFAAAAANPu+mss0tPTdfToURUvXlwWi8Xe5QAAAACFhmEYOn/+vHx9fVWkSPbHJO76YHH06NEsn7oKAAAA4NYOHz6sChUqZNvnrg8WxYsXl/TvD6NEiRJ2rgYAAAAoPJKTk+Xn52f9Tp2duz5YXD/9qUSJEgQLAAAA4Dbk5JICLt4GAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgml2DxdSpU1W3bl3rHZuCgoK0dOlS6/zLly9r4MCBKlOmjNzd3RUaGqoTJ07YsWIAAAAAmbFrsKhQoYLeeustbdmyRZs3b9ZDDz2kJ598Urt375YkDR06VN9//73mzZunuLg4HT16VE899ZQ9SwYAAACQCYthGIa9i7hR6dKl9e6776pz587y9PTU7Nmz1blzZ0nSH3/8oZo1a2rDhg164IEHcrS+5ORkeXh4KCkpiedYAAAAALmQm+/SBeYai7S0NM2ZM0cXLlxQUFCQtmzZoqtXr6pNmzbWPoGBgapYsaI2bNhgx0oBAAAA3MzuT97euXOngoKCdPnyZbm7u2vBggWqVauWtm/fLmdnZ5UsWdKmv7e3t44fP57l+lJTU5WammqdTk5Ozq/SAQAAAPwfux+xqFGjhrZv365NmzZpwIABCgsL0549e257fdHR0fLw8LC+/Pz88rBaAAAAAJmxe7BwdnZW1apV1ahRI0VHR6tevXr64IMP5OPjoytXrujcuXM2/U+cOCEfH58s1zdq1CglJSVZX4cPH87nPQAAAABg92Bxs/T0dKWmpqpRo0ZycnLSypUrrfMSEhL0119/KSgoKMvlXVxcrLevvf4CAAAAkL/seo3FqFGj1L59e1WsWFHnz5/X7NmztWbNGi1fvlweHh7q3bu3hg0bptKlS6tEiRIaNGiQgoKCcnxHKAAAAAB3hl2DxcmTJ9WzZ08dO3ZMHh4eqlu3rpYvX66HH35YkjRx4kQVKVJEoaGhSk1NVdu2bfXxxx/bs2QAAAAAmShwz7HIazzHAgAAALg9hfI5FgAAAAAKL7s/x+JeVGnkj/YuoUA7+FYHe5cAAACAXOKIBQAAAADTOGIBFEIc9coeR70AALjzOGIBAAAAwDSCBQAAAADTCBYAAAAATOMaCwC4x3CNzq1xnQ4A5B5HLAAAAACYxhELAACQKxz1yh5HvHCv4ogFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA07grFAAAAO4o7iyWvcJ6ZzGOWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADT7BosoqOjdf/996t48eLy8vJSx44dlZCQYNMnJCREFovF5tW/f387VQwAAAAgM3YNFnFxcRo4cKA2btyon3/+WVevXtUjjzyiCxcu2PTr27evjh07Zn298847dqoYAAAAQGYc7bnxZcuW2UzHxMTIy8tLW7ZsUatWraztxYoVk4+Pz50uDwAAAEAOFahrLJKSkiRJpUuXtmmPjY1V2bJlVbt2bY0aNUoXL17Mch2pqalKTk62eQEAAADIX3Y9YnGj9PR0DRkyRM2bN1ft2rWt7c8++6z8/f3l6+urHTt2KDIyUgkJCfruu+8yXU90dLSioqLuVNkAAAAAVICCxcCBA7Vr1y6tW7fOpv2FF16w/rtOnToqV66cWrdurcTERFWpUiXDekaNGqVhw4ZZp5OTk+Xn55d/hQMAAAAoGMEiIiJCP/zwg9auXasKFSpk27dp06aSpP3792caLFxcXOTi4pIvdQIAAADInF2DhWEYGjRokBYsWKA1a9aocuXKt1xm+/btkqRy5crlc3UAAAAAcsquwWLgwIGaPXu2Fi1apOLFi+v48eOSJA8PDxUtWlSJiYmaPXu2Hn30UZUpU0Y7duzQ0KFD1apVK9WtW9eepQMAAAC4gV2DxdSpUyX9+xC8G82YMUPh4eFydnbWihUrNGnSJF24cEF+fn4KDQ3VmDFj7FAtAAAAgKzY/VSo7Pj5+SkuLu4OVQMAAADgdhWo51gAAAAAKJwIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEyza7CIjo7W/fffr+LFi8vLy0sdO3ZUQkKCTZ/Lly9r4MCBKlOmjNzd3RUaGqoTJ07YqWIAAAAAmbFrsIiLi9PAgQO1ceNG/fzzz7p69aoeeeQRXbhwwdpn6NCh+v777zVv3jzFxcXp6NGjeuqpp+xYNQAAAICbOdpz48uWLbOZjomJkZeXl7Zs2aJWrVopKSlJ06dP1+zZs/XQQw9JkmbMmKGaNWtq48aNeuCBB+xRNgAAAICbFKhrLJKSkiRJpUuXliRt2bJFV69eVZs2bax9AgMDVbFiRW3YsCHTdaSmpio5OdnmBQAAACB/FZhgkZ6eriFDhqh58+aqXbu2JOn48eNydnZWyZIlbfp6e3vr+PHjma4nOjpaHh4e1pefn19+lw4AAADc8wpMsBg4cKB27dqlOXPmmFrPqFGjlJSUZH0dPnw4jyoEAAAAkBW7XmNxXUREhH744QetXbtWFSpUsLb7+PjoypUrOnfunM1RixMnTsjHxyfTdbm4uMjFxSW/SwYAAABwA7sesTAMQxEREVqwYIFWrVqlypUr28xv1KiRnJyctHLlSmtbQkKC/vrrLwUFBd3pcgEAAABkwa5HLAYOHKjZs2dr0aJFKl68uPW6CQ8PDxUtWlQeHh7q3bu3hg0bptKlS6tEiRIaNGiQgoKCuCMUAAAAUIDYNVhMnTpVkhQSEmLTPmPGDIWHh0uSJk6cqCJFiig0NFSpqalq27atPv744ztcKQAAAIDs5DpYHDhwQL/88osOHTqkixcvytPTUw0aNFBQUJBcXV1ztS7DMG7Zx9XVVVOmTNGUKVNyWyoAAACAOyTHwSI2NlYffPCBNm/eLG9vb/n6+qpo0aI6c+aMEhMT5erqqu7duysyMlL+/v75WTMAAACAAiZHwaJBgwZydnZWeHi4vv322wzPhkhNTdWGDRs0Z84cNW7cWB9//LG6dOmSLwUDAAAAKHhyFCzeeusttW3bNsv5Li4uCgkJUUhIiN544w0dPHgwr+oDAAAAUAjkKFhkFypuVqZMGZUpU+a2CwIAAABQ+Ji6K9SPP/6oNWvWKC0tTc2bN1doaGhe1QUAAACgELntB+S9+uqrGjFihCwWiwzD0NChQzVo0KC8rA0AAABAIZHjIxabN29W48aNrdNz585VfHy8ihYtKkkKDw9XSEiIPvroo7yvEgAAAECBluMjFv3799eQIUN08eJFSVJAQIDee+89JSQkaOfOnZo6daqqV6+eb4UCAAAAKLhyHCw2bdqkcuXKqWHDhvr+++/1xRdfaNu2bWrWrJlatmypI0eOaPbs2flZKwAAAIACKsenQjk4OCgyMlJdunTRgAED5ObmpsmTJ8vX1zc/6wMAAABQCOT64u2AgAAtX75cnTp1UqtWrTRlypT8qAsAAABAIZLjYHHu3DmNGDFCjz/+uMaMGaNOnTpp06ZN+v333/XAAw9o586d+VknAAAAgAIsx8EiLCxMmzZtUocOHZSQkKABAwaoTJkyiomJ0RtvvKFnnnlGkZGR+VkrAAAAgAIqx9dYrFq1Stu2bVPVqlXVt29fVa1a1TqvdevW2rp1q8aPH58vRQIAAAAo2HJ8xKJatWr69NNPtXfvXk2bNk3+/v42811dXfXmm2/meYEAAAAACr4cB4svvvhCq1atUoMGDTR79mxNnTo1P+sCAAAAUIjk+FSo+vXra/PmzflZCwAAAIBCKkdHLAzDyO86AAAAABRiOQoW9913n+bMmaMrV65k22/fvn0aMGCA3nrrrTwpDgAAAEDhkKNToT766CNFRkbqxRdf1MMPP6zGjRvL19dXrq6uOnv2rPbs2aN169Zp9+7dioiI0IABA/K7bgAAAAAFSI6CRevWrbV582atW7dOc+fOVWxsrA4dOqRLly6pbNmyatCggXr27Knu3burVKlS+V0zAAAAgAImxxdvS1KLFi3UokWL/KoFAAAAQCGV49vNAgAAAEBWCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANNuK1gkJiZqzJgx6tatm06ePClJWrp0qXbv3p2nxQEAAAAoHHIdLOLi4lSnTh1t2rRJ3333nVJSUiRJ8fHxGjduXJ4XCAAAAKDgy3WwGDlypCZMmKCff/5Zzs7O1vaHHnpIGzduzNPiAAAAABQOuQ4WO3fuVKdOnTK0e3l56Z9//smTogAAAAAULrkOFiVLltSxY8cytG/btk3ly5fPk6IAAAAAFC65DhZdu3ZVZGSkjh8/LovFovT0dP36668aPny4evbsmR81AgAAACjgch0s3nzzTQUGBsrPz08pKSmqVauWWrVqpWbNmmnMmDH5USMAAACAAs4xtws4Ozvrs88+09ixY7Vz506lpKSoQYMGqlatWn7UBwAAAKAQyPURi/Hjx+vixYvy8/PTo48+qqefflrVqlXTpUuXNH78+PyoEQAAAEABl+tgERUVZX12xY0uXryoqKioPCkKAAAAQOGS62BhGIYsFkuG9vj4eJUuXTpPigIAAABQuOT4GotSpUrJYrHIYrGoevXqNuEiLS1NKSkp6t+/f74UCQAAAKBgy3GwmDRpkgzD0PPPP6+oqCh5eHhY5zk7O6tSpUoKCgrKlyIBAAAAFGw5DhZhYWGSpMqVK6tZs2ZycnLKt6IAAAAAFC65vt1scHCw9d+XL1/WlStXbOaXKFHCfFUAAAAACpVcX7x98eJFRUREyMvLS25ubipVqpTNCwAAAMC9J9fB4pVXXtGqVas0depUubi46PPPP1dUVJR8fX01a9as/KgRAAAAQAGX61Ohvv/+e82aNUshISHq1auXWrZsqapVq8rf31+xsbHq3r17ftQJAAAAoADL9RGLM2fOKCAgQNK/11OcOXNGktSiRQutXbs2b6sDAAAAUCjkOlgEBATowIEDkqTAwEB98803kv49klGyZMk8LQ4AAABA4ZDrYNGrVy/Fx8dLkkaOHKkpU6bI1dVVQ4cO1SuvvJLnBQIAAAAo+HJ9jcXQoUOt/27Tpo3++OMPbdmyRVWrVlXdunXztDgAAAAAhUOug8XN/P395e/vL0maP3++OnfubLooAAAAAIVLrk6Funbtmnbt2qW9e/fatC9atEj16tXjjlAAAADAPSrHwWLXrl2qWrWq6tWrp5o1a+qpp57SiRMnFBwcrOeff17t27dXYmJiftYKAAAAoIDK8alQkZGRqlq1qiZPnqyvv/5aX3/9tf73v/+pd+/eWrZsmYoWLZqfdQIAAAAowHIcLH7//Xf99NNPql+/vlq2bKmvv/5ao0eP1nPPPZef9QEAAAAoBHJ8KtQ///wjX19fSZKHh4fc3Nz0wAMPmNr42rVr9fjjj8vX11cWi0ULFy60mR8eHi6LxWLzateunaltAgAAAMh7OT5iYbFYdP78ebm6usowDFksFl26dEnJyck2/UqUKJHjjV+4cEH16tXT888/r6eeeirTPu3atdOMGTOs0y4uLjlePwAAAIA7I8fBwjAMVa9e3Wa6QYMGNtMWi0VpaWk53nj79u3Vvn37bPu4uLjIx8cnx+sEAAAAcOflOFisXr06P+vI0po1a+Tl5aVSpUrpoYce0oQJE1SmTBm71AIAAAAgczkOFsHBwflZR6batWunp556SpUrV1ZiYqJGjx6t9u3ba8OGDXJwcMh0mdTUVKWmplqnbz5VCwAAAEDeM/3k7fzUtWtX67/r1KmjunXrqkqVKlqzZo1at26d6TLR0dGKioq6UyUCAAAAUC6fvG1vAQEBKlu2rPbv359ln1GjRikpKcn6Onz48B2sEAAAALg3FegjFjc7cuSITp8+rXLlymXZx8XFhTtHAQAAAHeYXYNFSkqKzdGHAwcOaPv27SpdurRKly6tqKgohYaGysfHR4mJiRoxYoSqVq2qtm3b2rFqAAAAADeza7DYvHmzHnzwQev0sGHDJElhYWGaOnWqduzYoZkzZ+rcuXPy9fXVI488otdff50jEgAAAEABk+tgceHCBb311ltauXKlTp48qfT0dJv5f/75Z47XFRISIsMwspy/fPny3JYHAAAAwA5yHSz69OmjuLg4PffccypXrpwsFkt+1AUAAACgEMl1sFi6dKl+/PFHNW/ePD/qAQAAAFAI5fp2s6VKlVLp0qXzoxYAAAAAhVSug8Xrr7+usWPH6uLFi/lRDwAAAIBCKNenQr333ntKTEyUt7e3KlWqJCcnJ5v5W7duzbPiAAAAABQOuQ4WHTt2zIcyAAAAABRmuQoW165dk8Vi0fPPP68KFSrkV00AAAAACplcXWPh6Oiod999V9euXcuvegAAAAAUQrm+ePuhhx5SXFxcftQCAAAAoJDK9TUW7du318iRI7Vz5041atRIbm5uNvOfeOKJPCsOAAAAQOGQ62Dx4osvSpLef//9DPMsFovS0tLMVwUAAACgUMl1sEhPT8+POgAAAAAUYrm+xgIAAAAAbpbrIxbjx4/Pdv7YsWNvuxgAAAAAhVOug8WCBQtspq9evaoDBw7I0dFRVapUIVgAAAAA96BcB4tt27ZlaEtOTlZ4eLg6deqUJ0UBAAAAKFzy5BqLEiVKKCoqSq+++mperA4AAABAIZNnF28nJSUpKSkpr1YHAAAAoBDJ9alQH374oc20YRg6duyYvvzyS7Vv3z7PCgMAAABQeOQ6WEycONFmukiRIvL09FRYWJhGjRqVZ4UBAAAAKDxyHSwOHDiQH3UAAAAAKMRyfY3F888/r/Pnz2dov3Dhgp5//vk8KQoAAABA4ZLrYDFz5kxdunQpQ/ulS5c0a9asPCkKAAAAQOGS41OhkpOTZRiGDMPQ+fPn5erqap2XlpamJUuWyMvLK1+KBAAAAFCw5ThYlCxZUhaLRRaLRdWrV88w32KxKCoqKk+LAwAAAFA45DhYrF69WoZh6KGHHtK3336r0qVLW+c5OzvL399fvr6++VIkAAAAgIItx8EiODhY0r93hapYsaIsFku+FQUAAACgcMn1xdv+/v5at26devTooWbNmunvv/+WJH355Zdat25dnhcIAAAAoODLdbD49ttv1bZtWxUtWlRbt25VamqqJCkpKUlvvvlmnhcIAAAAoODLdbCYMGGCpk2bps8++0xOTk7W9ubNm2vr1q15WhwAAACAwiHXwSIhIUGtWrXK0O7h4aFz587lRU0AAAAACplcBwsfHx/t378/Q/u6desUEBCQJ0UBAAAAKFxyHSz69u2rl156SZs2bZLFYtHRo0cVGxur4cOHa8CAAflRIwAAAIACLse3m71u5MiRSk9PV+vWrXXx4kW1atVKLi4uGj58uAYNGpQfNQIAAAAo4HIdLCwWi/7zn//olVde0f79+5WSkqJatWrJ3d1dly5dUtGiRfOjTgAAAAAFWK5PhbrO2dlZtWrVUpMmTeTk5KT3339flStXzsvaAAAAABQSOQ4WqampGjVqlBo3bqxmzZpp4cKFkqQZM2aocuXKmjhxooYOHZpfdQIAAAAowHJ8KtTYsWP1ySefqE2bNlq/fr26dOmiXr16aePGjXr//ffVpUsXOTg45GetAAAAAAqoHAeLefPmadasWXriiSe0a9cu1a1bV9euXVN8fLwsFkt+1ggAAACggMvxqVBHjhxRo0aNJEm1a9eWi4uLhg4dSqgAAAAAkPNgkZaWJmdnZ+u0o6Oj3N3d86UoAAAAAIVLjk+FMgxD4eHhcnFxkSRdvnxZ/fv3l5ubm02/7777Lm8rBAAAAFDg5ThYhIWF2Uz36NEjz4sBAAAAUDjlOFjMmDEjP+sAAAAAUIjd9gPyAAAAAOA6ggUAAAAA0wgWAAAAAEwjWAAAAAAwjWABAAAAwDSCBQAAAADTCBYAAAAATCNYAAAAADCNYAEAAADANIIFAAAAANMIFgAAAABMs2uwWLt2rR5//HH5+vrKYrFo4cKFNvMNw9DYsWNVrlw5FS1aVG3atNG+ffvsUywAAACALNk1WFy4cEH16tXTlClTMp3/zjvv6MMPP9S0adO0adMmubm5qW3btrp8+fIdrhQAAABAdhztufH27durffv2mc4zDEOTJk3SmDFj9OSTT0qSZs2aJW9vby1cuFBdu3a9k6UCAAAAyEaBvcbiwIEDOn78uNq0aWNt8/DwUNOmTbVhw4Ysl0tNTVVycrLNCwAAAED+KrDB4vjx45Ikb29vm3Zvb2/rvMxER0fLw8PD+vLz88vXOgEAAAAU4GBxu0aNGqWkpCTr6/Dhw/YuCQAAALjrFdhg4ePjI0k6ceKETfuJEyes8zLj4uKiEiVK2LwAAAAA5K8CGywqV64sHx8frVy50tqWnJysTZs2KSgoyI6VAQAAALiZXe8KlZKSov3791unDxw4oO3bt6t06dKqWLGihgwZogkTJqhatWqqXLmyXn31Vfn6+qpjx472KxoAAABABnYNFps3b9aDDz5onR42bJgkKSwsTDExMRoxYoQuXLigF154QefOnVOLFi20bNkyubq62qtkAAAAAJmwa7AICQmRYRhZzrdYLBo/frzGjx9/B6sCAAAAkFsF9hoLAAAAAIUHwQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBTpYvPbaa7JYLDavwMBAe5cFAAAA4CaO9i7gVu677z6tWLHCOu3oWOBLBgAAAO45Bf5buqOjo3x8fOxdBgAAAIBsFOhToSRp37598vX1VUBAgLp3766//vor2/6pqalKTk62eQEAAADIXwU6WDRt2lQxMTFatmyZpk6dqgMHDqhly5Y6f/58lstER0fLw8PD+vLz87uDFQMAAAD3pgIdLNq3b68uXbqobt26atu2rZYsWaJz587pm2++yXKZUaNGKSkpyfo6fPjwHawYAAAAuDcV+GssblSyZElVr15d+/fvz7KPi4uLXFxc7mBVAAAAAAr0EYubpaSkKDExUeXKlbN3KQAAAABuUKCDxfDhwxUXF6eDBw9q/fr16tSpkxwcHNStWzd7lwYAAADgBgX6VKgjR46oW7duOn36tDw9PdWiRQtt3LhRnp6e9i4NAAAAwA0KdLCYM2eOvUsAAAAAkAMF+lQoAAAAAIUDwQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBpBAsAAAAAphEsAAAAAJhGsAAAAABgGsECAAAAgGkECwAAAACmESwAAAAAmEawAAAAAGAawQIAAACAaQQLAAAAAKYRLAAAAACYRrAAAAAAYBrBAgAAAIBphSJYTJkyRZUqVZKrq6uaNm2q3377zd4lAQAAALhBgQ8Wc+fO1bBhwzRu3Dht3bpV9erVU9u2bXXy5El7lwYAAADg/xT4YPH++++rb9++6tWrl2rVqqVp06apWLFi+uKLL+xdGgAAAID/U6CDxZUrV7Rlyxa1adPG2lakSBG1adNGGzZssGNlAAAAAG7kaO8CsvPPP/8oLS1N3t7eNu3e3t76448/Ml0mNTVVqamp1umkpCRJUnJycv4VmkvpqRftXUKBVpDeq4KKMZQ9xlD2GD+3xhjKHmMoe4yfW2MMZa8gjaHrtRiGccu+BTpY3I7o6GhFRUVlaPfz87NDNbgdHpPsXQEKO8YQzGIMwQzGD8wqiGPo/Pnz8vDwyLZPgQ4WZcuWlYODg06cOGHTfuLECfn4+GS6zKhRozRs2DDrdHp6us6cOaMyZcrIYrHka72FUXJysvz8/HT48GGVKFHC3uWgEGIMwQzGD8xiDMEsxlD2DMPQ+fPn5evre8u+BTpYODs7q1GjRlq5cqU6duwo6d+gsHLlSkVERGS6jIuLi1xcXGzaSpYsmc+VFn4lSpTgfyaYwhiCGYwfmMUYglmMoazd6kjFdQU6WEjSsGHDFBYWpsaNG6tJkyaaNGmSLly4oF69etm7NAAAAAD/p8AHi2eeeUanTp3S2LFjdfz4cdWvX1/Lli3LcEE3AAAAAPsp8MFCkiIiIrI89QnmuLi4aNy4cRlOHwNyijEEMxg/MIsxBLMYQ3nHYuTk3lEAAAAAkI0C/YA8AAAAAIUDwQIAAACAaQQLAMAdUalSJU2aNMneZQAA8gnBopCKjo7W/fffr+LFi8vLy0sdO3ZUQkKCTZ+QkBBZLBabV//+/bNdb0JCgh588EF5e3vL1dVVAQEBGjNmjK5evZpp/zlz5shisVifM4LCY+rUqapbt671vt1BQUFaunSpdf7tjJ8b7d+/X8WLF8/2OTKMn4IlJCREQ4YMydAeExNToJ8HtGbNGj355JMqV66c3NzcVL9+fcXGxtr0iYmJyTCeXV1d7VQxsvPaa69leK8CAwOt883+bsLd6a233pLFYrH5HXY7Y+XgwYMZlrFYLNq4cWOm/fkcs1Uo7gqFjOLi4jRw4EDdf//9unbtmkaPHq1HHnlEe/bskZubm7Vf3759NX78eOt0sWLFsl2vk5OTevbsqYYNG6pkyZKKj49X3759lZ6erjfffNOm78GDBzV8+HC1bNkyb3cOd0SFChX01ltvqVq1ajIMQzNnztSTTz6pbdu26b777pOU+/Fz3dWrV9WtWze1bNlS69evz7QP4we5deXKFTk7O2doX79+verWravIyEh5e3vrhx9+UM+ePeXh4aHHHnvM2q9EiRI2f4CxWCx3pG7k3n333acVK1ZYpx0dbb+u5OZ305o1axQeHq6DBw/meZ0oGH7//Xd98sknqlu3boZ5t/s5tmLFCutnoSSVKVMmQx8+xzIiWBRSy5Yts5mOiYmRl5eXtmzZolatWlnbixUrJh8fnxyvNyAgQAEBAdZpf39/rVmzRr/88otNv7S0NHXv3l1RUVH65ZdfdO7cudvbEdjN448/bjP9xhtvaOrUqdq4caP1l2lux891Y8aMUWBgoFq3bp1psGD8FG7h4eE6d+6cWrRooffee09XrlxR165dNWnSJDk5OUmSTp48qd69e2vFihXy8fHRhAkTMqzn3LlzGj58uBYtWqTU1FQ1btxYEydOVL169ST9+5frhQsXKiIiQm+88YYOHTqk9PT0DOsZPXq0zfRLL72kn376Sd99951NsLBYLLc1nnHnOTo6Zvte3e7vJtx9UlJS1L17d3322WeZ/p653bFSpkyZbJfjcyxznAp1l0hKSpIklS5d2qY9NjZWZcuWVe3atTVq1ChdvHgxV+vdv3+/li1bpuDgYJv28ePHy8vLS7179zZXOAqEtLQ0zZkzRxcuXFBQUJC1/XbGz6pVqzRv3jxNmTIlyz6Mn8Jv9erVSkxM1OrVqzVz5kzFxMQoJibGOj88PFyHDx/W6tWrNX/+fH388cc6efKkzTq6dOmikydPaunSpdqyZYsaNmyo1q1b68yZM9Y++/fv17fffqvvvvtO27dvz3F9SUlJGX4fpqSkyN/fX35+fnryySe1e/fu29p35L99+/bJ19dXAQEB6t69u/766y+b+WY/23D3GDhwoDp06KA2bdpkOv92x8oTTzwhLy8vtWjRQosXL84wn8+xzHHE4i6Qnp6uIUOGqHnz5qpdu7a1/dlnn5W/v798fX21Y8cORUZGKiEhQd99990t19msWTNt3bpVqampeuGFF2wOI65bt07Tp0/P1Yc8CqadO3cqKChIly9flru7uxYsWKBatWpJur3xc/r0aYWHh+urr75SiRIl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yHE9H3/8sbZv367nn39eFy9etJnXqFEjm+n//e9/CgoKsjmy0bx5c6WkpOjIkSM53qYkBQUFZZjmiAUA3B5HexcAALjzpk+frmvXrtlcrG0YhlxcXDR58mR5eHjkaD0pKSnq16+fBg8enGFexYoVM12mWrVqSkhIsGkrV66cJKl06dIZ+ru5ueWolhsVKVJEN9+b5OrVq7leDwAg5zhiAQD3mGvXrmnWrFl67733tH37dusrPj5evr6++vrrryVJNWrU0ObNm22W/f33322mGzZsqD179qhq1aoZXlndvalbt276+eeftW3bttuqv2bNmtqwYYNNcPj1119VvHhxVahQQZLk6empY8eOWecnJydnegRl48aNGaZr1qx5W3UBwL2OYAEA95gffvhBZ8+eVe/evVW7dm2bV2hoqPV0qH79+umPP/5QZGSk9u7dq2+++cZ656jrpyFFRkZq/fr1ioiI0Pbt27Vv3z4tWrQo24u3hw4dqqCgILVu3VoffPCBtm7dqgMHDmj58uVaunSpHBwcsq3/xRdf1OHDhzVo0CD98ccfWrRokcaNG6dhw4apSJF/P9Yeeughffnll/rll1+0c+dOhYWFZbreefPm6YsvvtDevXs1btw4/fbbb9nWDgDIGsECAO4x06dPV5s2bTI93Sk0NFSbN2/Wjh07VLlyZc2fP1/fffed6tatq6lTp1rvCuXi4iJJqlu3ruLi4rR37161bNlSDRo00NixY7N9Hoarq6tWrlypyMhIzZgxQy1atFDNmjU1ZMgQNW/eXAsXLsy2/vLly2vJkiX67bffVK9ePfXv31+9e/fWmDFjrH1GjRql4OBgPfbYY+rQoYM6duyoKlWqZFhXVFSU5syZo7p162rWrFn6+uuvVatWrZz8GAEAN+EBeQCAHHvjjTc0bdo0HT582N6lmGaxWLRgwQJ17NjR3qUAwF2Bi7cBAFn6+OOPdf/996tMmTL69ddf9e6773KqEAAgUwQLAECW9u3bpwkTJujMmTOqWLGiXn75ZY0aNcreZQEACiBOhQIAAABgGhdvAwAAADCNYAEAAADANIIFAAAAANMIFgAAAABMI1gAAAAAMI1gAQAAAMA0ggUAAAAA0wgWAAAAAEwjWAAAAAAw7f8BrTiqBvfnMB8AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "discount_return_rate = (\n",
        "    df.groupby('Discount_Applied')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(discount_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EvgMItrEdj5B",
        "outputId": "b2a00688-feb5-42ff-a694-2c41c8154c8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Discount_Applied\n",
            "0.54     100.0\n",
            "0.05     100.0\n",
            "0.07     100.0\n",
            "0.35     100.0\n",
            "49.79    100.0\n",
            "         ...  \n",
            "28.93      0.0\n",
            "28.90      0.0\n",
            "29.31      0.0\n",
            "29.28      0.0\n",
            "29.13      0.0\n",
            "Name: Return_Status, Length: 3177, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "discount_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Discount')\n",
        "plt.xlabel('Discount Level')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "Yx-0CFJKdpAW",
        "outputId": "f59c786a-02f7-4e17-dc67-1ba6b498f955"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAxUAAAHqCAYAAAByRmPvAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAX+9JREFUeJzt3Xd0VHX+//HXTDKTXgikASEJCII0QRSRIiKIiKyuIIuiFF1ABAtKsQACKigqKop1VXQBXdG1K0oRd7GgFFmQrkERgQAhvWc+vz/4zf1mSIIkN5AAz8c59yRzy2fe986dO/c1t4zDGGMEAAAAAFXkrOkCAAAAAJzaCBUAAAAAbCFUAAAAALCFUAEAAADAFkIFAAAAAFsIFQAAAABsIVQAAAAAsIVQAQAAAMAWQgUAAAAAWwgVAIAaM2zYMIWGhtZ0GeVyOByaNm1aTZcBAKcEQgWA09r8+fPlcDiszt/fXw0aNNCwYcO0Z8+eKrW5efNmTZs2Tbt27areYqtJUlKSzzyHhIToggsu0BtvvFHlNj/99NNTege79DJxOp2KjIxU69atNXLkSK1evbqmyztpvvnmG02bNk3p6ek1XQqA04x/TRcAACfDjBkzlJycrPz8fH333XeaP3++Vq1apU2bNikwMLBSbW3evFnTp09X9+7dlZSUdGIKtuncc8/V3XffLUnau3ev/vGPf2jo0KEqKCjQiBEjKt3ep59+qnnz5p3SwaL0MsnKytKWLVu0ePFivfzyyxo3bpzmzJnjM35eXp78/U+vj8lvvvlG06dP17BhwxQZGVnT5QA4jZxeW0sAqECfPn3UoUMHSdLf//531atXT48++qg+/PBDDRw4sIarOyInJ0chISHV0laDBg10ww03WI+HDRumxo0b68knn6xSqDgdHL1MJOnRRx/V9ddfryeffFJNmzbV6NGjrWGVDZsAcCbj9CcAZ6SuXbtKkn7++Wef/lu3btWAAQMUFRWlwMBAdejQQR9++KE1fP78+br22mslSZdccol1Ss3KlSslVXweflJSkoYNG+bTjsPh0FdffaVbb71VMTExatiwoSSpe/fuatWqlTZv3qxLLrlEwcHBatCggWbPnl3l+Y2Ojlbz5s3LzO9///tfXXvttWrUqJECAgKUkJCgcePGKS8vzxpn2LBhmjdvnjV/3s7L4/HoqaeeUsuWLRUYGKjY2FiNGjVKhw8fPu76fvnlF/Xu3VshISGqX7++ZsyYIWOMJMkYo6SkJF111VVlpsvPz1dERIRGjRpVqeXhFRQUpH/+85+KiorSww8/bD2nd15Lv5ZZWVm68847lZSUpICAAMXExKhXr15at26dT5urV6/WFVdcoTp16igkJERt2rTR008/7TPOihUr1LVrV4WEhCgyMlJXXXWVtmzZ4jPOsGHDyj0SNm3aNJ/l76117Nixev/999WqVSsFBASoZcuWWrJkic90EyZMkCQlJydbr2NtPY0PwKmFIxUAzkjeHak6depY/X766Sd17txZDRo00D333KOQkBC9/fbbuvrqq/Xuu+/qr3/9q7p166bbb79dc+fO1X333acWLVpIkvW3sm699VZFR0dr6tSpysnJsfofPnxYl19+ua655hoNHDhQ77zzjiZNmqTWrVurT58+lX6e4uJi/f777z7zK0mLFy9Wbm6uRo8erbp16+r777/XM888o99//12LFy+WJI0aNUp//PGHli5dqn/+859l2h41apTmz5+v4cOH6/bbb1dKSoqeffZZrV+/Xl9//bVcLtcxayspKdHll1+uCy+8ULNnz9aSJUv0wAMPqLi4WDNmzJDD4dANN9yg2bNnKy0tTVFRUda0H330kTIzM8scgaiM0NBQ/fWvf9Urr7yizZs3q2XLluWOd8stt+idd97R2LFjdc455+jQoUNatWqVtmzZovbt20uSli5dqiuvvFLx8fG64447FBcXpy1btujjjz/WHXfcIUlatmyZ+vTpo8aNG2vatGnKy8vTM888o86dO2vdunVVPqVu1apV+ve//61bb71VYWFhmjt3rvr376/ffvtNdevW1TXXXKPt27frzTff1JNPPql69epJOhI4AcA2AwCnsddee81IMsuWLTMHDhwwu3fvNu+8846Jjo42AQEBZvfu3da4l156qWndurXJz8+3+nk8HnPRRReZpk2bWv0WL15sJJkvv/yyzPNJMg888ECZ/omJiWbo0KFl6urSpYspLi72Gffiiy82kswbb7xh9SsoKDBxcXGmf//+fzrPiYmJ5rLLLjMHDhwwBw4cMBs3bjQ33nijkWTGjBnjM25ubm6Z6WfNmmUcDof59ddfrX5jxowx5X1k/Pe//zWSzMKFC336L1mypNz+Rxs6dKiRZG677Tarn8fjMX379jVut9scOHDAGGPMtm3bjCTz/PPP+0z/l7/8xSQlJRmPx3PM50lMTDR9+/atcPiTTz5pJJkPPvjA6nf0axkREVFm+ZVWXFxskpOTTWJiojl8+LDPsNL1nXvuuSYmJsYcOnTI6rdhwwbjdDrNkCFDrH5Dhw41iYmJZZ7ngQceKPNaSDJut9vs3LnTp01J5plnnrH6PfbYY0aSSUlJqXA+AKAqOP0JwBmhZ8+eio6OVkJCggYMGKCQkBB9+OGH1ilHaWlpWrFihQYOHKisrCwdPHhQBw8e1KFDh9S7d2/t2LGjyneLOpYRI0bIz8+vTP/Q0FCfb9/dbrcuuOAC/fLLL8fV7hdffKHo6GhFR0erdevW+uc//6nhw4frscce8xkvKCjI+j8nJ0cHDx7URRddJGOM1q9f/6fPs3jxYkVERKhXr17WMjt48KDOO+88hYaG6ssvvzyueseOHWv97z2Vp7CwUMuWLZMkNWvWTB07dtTChQut8dLS0vTZZ59p8ODBZU4HqizvbW2zsrIqHCcyMlKrV6/WH3/8Ue7w9evXKyUlRXfeeWeZi6C99e3du1c//vijhg0b5nPEpU2bNurVq5c+/fTTKs9Dz5491aRJE582w8PDj3udAQA7CBUAzgjz5s3T0qVL9c477+iKK67QwYMHFRAQYA3fuXOnjDGaMmWKtTPu7R544AFJUmpqarXXlZycXG7/hg0bltlRrlOnznFfp9CxY0ctXbpUS5Ys0eOPP67IyEgdPnxYbrfbZ7zffvvN2sENDQ1VdHS0Lr74YklSRkbGnz7Pjh07lJGRoZiYmDLLLTs7+7iWmdPpVOPGjX36NWvWTJJ8zvcfMmSIvv76a/3666+SjgSaoqIi3XjjjX/6HH8mOztbkhQWFlbhOLNnz9amTZuUkJCgCy64QNOmTfPZYfder9KqVasK2/DWfvbZZ5cZ1qJFCx08eNDnNLjKaNSoUZl+lVlnAMAOrqkAcEa44IILrLs/XX311erSpYuuv/56bdu2TaGhofJ4PJKk8ePHq3fv3uW2cdZZZ1X5+UtKSsrtX/pIQWnlHb2Q5HMh8bHUq1dPPXv2lCT17t1bzZs315VXXqmnn35ad911l1VTr169lJaWpkmTJql58+YKCQnRnj17NGzYMGuZHIvH41FMTIzPEYTSqvN8/UGDBmncuHFauHCh7rvvPi1YsEAdOnQodwe9sjZt2iTp2K/xwIED1bVrV7333nv64osv9Nhjj+nRRx/Vv//97ypd5/JnKjr6UtG6ZHedAQA7CBUAzjh+fn6aNWuWLrnkEj377LO65557rG/KXS6XtTNekWOdalOnTp0yPyxWWFiovXv32q7bjr59++riiy/WzJkzNWrUKIWEhGjjxo3avn27Xn/9dQ0ZMsQad+nSpWWmr2iemzRpomXLlqlz584VBqQ/4/F49Msvv1hHJyRp+/btkuRz0XJUVJT69u2rhQsXavDgwfr666/11FNPVek5S8vOztZ7772nhISEP73gPj4+XrfeeqtuvfVWpaamqn379nr44YfVp08f69SjTZs2VbgOJSYmSpK2bdtWZtjWrVtVr14967bC5a1L0v8d7agKu6eJAUBFOP0JwBmpe/fuuuCCC/TUU08pPz9fMTEx6t69u1588cVyA8CBAwes/707feXt8DVp0kT/+c9/fPq99NJLFX67fDJNmjRJhw4d0ssvvyzp/77ZLv1NtjGmzO1PpYrneeDAgSopKdGDDz5YZpri4uLj/uXmZ5991qeGZ599Vi6XS5deeqnPeDfeeKM2b96sCRMmyM/PT4MGDTqu9iuSl5enG2+8UWlpabr//vuPeXTg6NPBYmJiVL9+fRUUFEiS2rdvr+TkZD311FNl5tu7jOPj43Xuuefq9ddf9xln06ZN+uKLL3TFFVdY/Zo0aaKMjAz973//s/rt3btX7733XpXn91jrLgDYwZEKAGesCRMm6Nprr9X8+fN1yy23aN68eerSpYtat26tESNGqHHjxtq/f7++/fZb/f7779qwYYOkI7/M7Ofnp0cffVQZGRkKCAhQjx49FBMTo7///e+65ZZb1L9/f/Xq1UsbNmzQ559/bt2+syb16dNHrVq10pw5czRmzBg1b95cTZo00fjx47Vnzx6Fh4fr3XffLfcc/PPOO0+SdPvtt6t3797WDv3FF1+sUaNGadasWfrxxx912WWXyeVyaceOHVq8eLGefvppDRgw4Jh1BQYGasmSJRo6dKg6duyozz77TJ988onuu+++MqdP9e3bV3Xr1tXixYvVp08fxcTEHPf879mzRwsWLJB05OjE5s2btXjxYu3bt0933333MX/rIisrSw0bNtSAAQPUtm1bhYaGatmyZfrhhx/0xBNPSDpybcjzzz+vfv366dxzz9Xw4cMVHx+vrVu36qefftLnn38uSXrsscfUp08fderUSTfffLN1S9mIiAif38UYNGiQJk2apL/+9a+6/fbblZubq+eff17NmjUr89sYx8v7Ot5///0aNGiQXC6X+vXrV20/ugjgDFZzN54CgBPPe+vWH374ocywkpIS06RJE9OkSRPrtq4///yzGTJkiImLizMul8s0aNDAXHnlleadd97xmfbll182jRs3Nn5+fj63ly0pKTGTJk0y9erVM8HBwaZ3795m586dFd5Stry6Lr74YtOyZcsy/Su6xejRjnX71Pnz5xtJ5rXXXjPGGLN582bTs2dPExoaaurVq2dGjBhh3YrUO44xR26Xetttt5no6GjjcDjK3NL0pZdeMuedd54JCgoyYWFhpnXr1mbixInmjz/+OGatQ4cONSEhIebnn382l112mQkODjaxsbHmgQceMCUlJeVOc+uttxpJZtGiRX+6LEovE0lGknE4HCY8PNy0bNnSjBgxwqxevbrcaVTqlrIFBQVmwoQJpm3btiYsLMyEhISYtm3bmueee67MdKtWrTK9evWyxmvTpo3PbV2NMWbZsmWmc+fOJigoyISHh5t+/fqZzZs3l2nriy++MK1atTJut9ucffbZZsGCBRXeUra8290evd4ZY8yDDz5oGjRoYJxOJ7eXBVBtHMZwBRcA4NQxbtw4vfLKK9q3b5+Cg4NruhwAgLimAgBwCsnPz9eCBQvUv39/AgUA1CJcUwEAqPVSU1O1bNkyvfPOOzp06JDuuOOOmi4JAFAKoQIAUOtt3rxZgwcPVkxMjObOnatzzz23pksCAJTCNRUAAAAAbOGaCgAAAAC2ECoAAAAA2MI1FZI8Ho/++OMPhYWFVfhrqgAAAMCpwBijrKws1a9fX07nyTmGQKiQ9McffyghIaGmywAAAACqze7du9WwYcOT8lyECklhYWGSjiz48PDwGq4GAAAAqLrMzEwlJCRY+7gnA6FCsk55Cg8PJ1QAAADgtHAyT+vnQm0AAAAAthAqAAAAANhCqAAAAABgC6ECAAAAgC2ECgAAAAC2ECoAAAAA2EKoAAAAAGALoQIAAACALYQKAAAAALYQKgAAAADYQqgAAAAAYEuNhor//Oc/6tevn+rXry+Hw6H333/fZ7gxRlOnTlV8fLyCgoLUs2dP7dixw2ectLQ0DR48WOHh4YqM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+9vfNGnSpBNVKwAAAIBaqFLXVKxYsULr16/XWWedpREjRuiss86yhl166aVat26dZsyYUe1FAgAAAKi9KnWkomnTpnrppZe0fft2vfDCC0pMTPQZHhgYqJkzZ1ZrgQAAAABqt0qFildffVUrVqxQu3bttGjRIj3//PMnqi4AAAAAp4hKnf507rnnas2aNSeqFgAAAACnoOM+UmGMOZF1AAAAADhFHXeoaNmypd566y0VFhYec7wdO3Zo9OjReuSRR2wXBwAAAKD2O+7Tn5555hlNmjRJt956q3r16qUOHTqofv36CgwM1OHDh7V582atWrVKP/30k8aOHavRo0efyLoBAAAA1BLHHSouvfRSrVmzRqtWrdK//vUvLVy4UL/++qvy8vJUr149tWvXTkOGDNHgwYNVp06dE1kzAAAAgFqkUhdqS1KXLl3UpUuXE1FLufbs2aNJkybps88+U25urs466yy99tpr6tChg6Qj13o88MADevnll5Wenq7OnTvr+eefV9OmTU9ajQAAAMCZrFK3lD3ZDh8+rM6dO8vlcumzzz7T5s2b9cQTT/gcCZk9e7bmzp2rF154QatXr1ZISIh69+6t/Pz8GqwcAAAAOHNU+kjFyfToo48qISFBr732mtUvOTnZ+t8Yo6eeekqTJ0/WVVddJUl64403FBsbq/fff1+DBg066TUDAAAAZ5pafaTiww8/VIcOHXTttdcqJiZG7dq108svv2wNT0lJ0b59+9SzZ0+rX0REhDp27Khvv/22wnYLCgqUmZnp0wEAAAComlodKn755Rfr+ojPP/9co0eP1u23367XX39dkrRv3z5JUmxsrM90sbGx1rDyzJo1SxEREVaXkJBw4mYCAAAAOM3V6lDh8XjUvn17zZw5U+3atdPIkSM1YsQIvfDCC7bavffee5WRkWF1u3fvrqaKAQAAgDNPlUPFzz//rMmTJ+u6665TamqqJOmzzz7TTz/9VG3FxcfH65xzzvHp16JFC/3222+SpLi4OEnS/v37fcbZv3+/Naw8AQEBCg8P9+kAAAAAVE2VQsVXX32l1q1ba/Xq1fr3v/+t7OxsSdKGDRv0wAMPVFtxnTt31rZt23z6bd++XYmJiZKOXLQdFxen5cuXW8MzMzO1evVqderUqdrqAAAAAFCxKoWKe+65Rw899JCWLl0qt9tt9e/Ro4e+++67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wKmjUqc/ZWZmyhgjY4yysrIUGBhoDSspKdGnn36qmJiYai8SAAAAQO1VqVARGRkph8Mhh8OhZs2alRnucDg0ffr0aisOAAAAQO1XqVDx5ZdfyhijHj166N1331VUVJQ1zO12KzExUfXr16/2IgEAAADUXpUKFRdffLGkI3d/atSokRwOxwkpCgAAAMCpo0oXaicmJmrVqlW64YYbdNFFF2nPnj2SpH/+859atWpVtRYIAAAAoHarUqh499131bt3bwUFBWndunUqKCiQJGVkZGjmzJnVWmBpjzzyiBwOh+68806rX35+vsaMGaO6desqNDRU/fv31/79+09YDQAAAAB8VSlUPPTQQ3rhhRf08ssvy+VyWf07d+6sdevWVVtxpf3www968cUX1aZNG5/+48aN00cffaTFixfrq6++0h9//KFrrrnmhNQAAAAAoKwqhYpt27apW7duZfpHREQoPT3dbk1lZGdna/DgwXr55ZdVp04dq39GRoZeeeUVzZkzRz169NB5552n1157Td98842+++67aq8DAAAAQFlVChVxcXHauXNnmf6rVq1S48aNbRd1tDFjxqhv377q2bOnT/+1a9eqqKjIp3/z5s3VqFEjffvtt9VeBwAAAICyKnX3J68RI0bojjvu0KuvviqHw6E//vhD3377rcaPH68pU6ZUa4FvvfWW1q1bpx9++KHMsH379sntdisyMtKnf2xsrPbt21dhmwUFBdZ1INKRH/UDAAAAUDVVChX33HOPPB6PLr30UuXm5qpbt24KCAjQ+PHjddttt1Vbcbt379Ydd9yhpUuX+vx6t12zZs3iR/qAU1TSPZ9o1yN9a7oMAABQSpVOf3I4HLr//vuVlpamTZs26bvvvtOBAwf04IMPKi8vr9qKW7t2rVJTU9W+fXv5+/vL399fX331lebOnSt/f3/FxsaqsLCwzHUc+/fvV1xcXIXt3nvvvcrIyLC63bt3V1vNAAAAwJmmSkcqvNxut8455xxJR04pmjNnjmbPnn3MU48q49JLL9XGjRt9+g0fPlzNmzfXpEmTlJCQIJfLpeXLl6t///6SjlxE/ttvv6lTp04VthsQEKCAgIBqqREAAAA401UqVBQUFGjatGlaunSp3G63Jk6cqKuvvlqvvfaa7r//fvn5+WncuHHVVlxYWJhatWrl0y8kJER169a1+t988826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iIgIa/0ur4aMjAw5HA5rO2CMUZ06dXw+u40x1navdE25ubnWe6P0vpW3Fu/yk6QdO3aoqKhIrVq10uHDh+VyuXw+j73LvvT+lnffIyMjQwcOHFBubq5iYmKszyrvtsy7LTy6Pju4+1MFXnvtNS1ZskQvvvii9SJ6dxYLCgp06NAhrV+/Xm+99ZYaNWqkOXPm6Ouvv9a0adOUmpqqWbNmac+ePeratatSUlK0bds2TZs2zXpjzpkzRy1bttSbb76pZcuWqXfv3nr11VcVHh6u9u3b680339Srr76qBx98UIWFhQoMDNQll1yiDRs26Oyzz9auXbuUmJioLl266Omnn5YxRu3atVOrVq104YUXasKECcrOztaYMWM0Z84cZWdnq3Pnztq5c6emTp2qxMREbd++XbNnz9b555+vSy+9VH5+fpo4caI6duyow4cPq379+urSpYv+97//KTQ0VGlpaQoPD9fixYv1wQcfyOVyaevWrerWrZvy8/MVGRlp7Zi+9957OuecczRx4kTdcMMNGjlypPbu3avNmzdryZIl2rJli9LT0zVgwAAlJCQoPDxcZ599ts4++2ytWbNGWVlZ2r9/v9xut3bs2KFPPvlEo0aN0qxZszR9+nQFBgbK5XKpbdu2Ovvss7V7925t2rRJW7du1X/+8x/NnDlTaWlpysvL02+//abFixerb9+++uSTTxQfH6/OnTvr3HPP1aZNm/Taa68pIyNDPXr00MSJE+Xv76/s7Gz9+OOPev7559WwYUNt375d+/bt0/nnn69OnTopKipKDz/8sG655RYlJyfrf//7n5KTk/XDDz/oxRdf1M033yyHw6HAwEC9+OKLGjJkiN566y0lJSUpLS1NkydP1sGDB/WXv/xF69ev18MPP6yhQ4cqLCxM+fn52rp1qxo1aqQFCxYoNjZWd955p3bt2qWHH35YDz74oBISEjRx4kQNGzZMdevW1bx589SsWTM1adJEnTp10uOPP64hQ4bo119/1VVXXaURI0bI5XJp8uTJWrFihQ4fPqzu3bvL7Xbr66+/1tatW7V3714VFxera9eu+te//qUBAwYoPj5en332me644w5lZWUpOztbTzzxhJo0aaKwsDAFBQVp9erVioqKUs+ePdWrVy/l5eUpISFBN954o/Ly8jRy5Eg999xzmjBhgubPny9/f3/16tVLr7/+uiZPnqx9+/bpxx9/VEJCgtq1a6dLLrlEWVlZmj59uqKiovTQQw9p+fLlWrlypRYtWqSBAwfqlltu0W+//ab77rtPgwcPVmhoqBYuXKiRI0cqPj5eH3zwgX788UelpqaqTp06OnjwoFq0aGGF5szMTJ177rlKSUnRyJEj9corr2jSpElyu93KzMzUgAEDtHfvXoWFhWn//v3atGmTGjdurDFjxmjWrFn65JNPNHfuXMXGxuqaa65R69at5efnp6VLl6pJkybav3+/du/erf/+978aMmSI/vKXv6hdu3ZKS0vT999/b+0MZmZm6uuvv9bMmTO1cuVKpaen68UXX5TT6dTkyZMVEBCgfv36ad26dXrvvfd04403qlmzZkpLS9OKFSv0xhtv6LffftM999wjf39/Pf300xoxYoSWLl2qJ554Qr/++qv69++vjIwMFRUVKSAgQJ9++qkk6bnnnlNMTIxGjx6thQsXavny5QoJCVFWVpYGDx6szz//XEuXLlV4eLhat24tSfrkk0+0ePFi3XbbbZo7d67OO+88rV27VtnZ2brpppuUnp6ubdu2qX379vrll1+0ZcsWvfzyyzpw4IBmzpypnj17KiQkRB9//LHee+89DR06VMnJycrOzlZ6erqSk5O1bds2TZgwQS1atNBjjz2muLg4ZWVlKSAgQP/73/+0adMmhYaGat++ffryyy81efJkRUVFqaCgQKtWrVKLFi101llnadOmTUpJSVHz5s2Vmpqqe+65R3Xr1lXPnj110003KTIyUm63Wy6XSytXrlRubq4uu+wyORwO7dy5UytXrtSvv/6q0NBQPfbYY2rWrJl+++03RUVF6f7779eKFSu0YsUKNW/eXFu2bJExRo0bN9Ynn3yi0NBQffDBB3rkkUeUl5en0NBQDR8+XFlZWZo1a5YyMzM1Z84c9e7dW4WFhTrrrLP0xRdf6LrrrlN2drbcbrcSExP13HPP6V//+pdWrFihUaNGafLkyWrQoIH8/Pz097//XRs2bNDOnTs1ffp0BQcHa9myZVq4cKGaNWumw4cPa+fOnXrmmWdUWFio6dOna+LEicrMzFTnzp21cuVKvffee1q4cKEOHz6svXv3KisrSy+++KIiIiK0evVqFRYW6vHHH1d8fLzefPNNNWjQQLGxsdq4caPuuusutW7dWr/88ouWLVumzz//XF27dlVsbKzWrFmjzz//XM2aNVOnTp20bt06vf/++2rXrp1mzpyp8ePHa+TIkdqxY4eGDBmixx57TNHR0fL399dLL72knJwcdezYUaNHj1ZUVJRyc3OVkJCgu+66Sy+88IJ2796tKVOm6Pbbb9cDDzyg3NxcNWnSRE2bNtXKlSt1880366efftLTTz+ttLQ0XXvttbr++ut1880366uvvtK//vUvffHFF7riiit00003KSsrS6+++qoOHjyoF154QWlpafrhhx/Upk0bGWP05Zdf6sMPP1RJSYmCgoI0b9487dmzRy+99JK2bt2qwsJC5eTkKCkpSXv37lXz5s3ldrs1cuRIZWVl6f3339ewYcP0888/66233lK/fv0UGBioOnXqaPPmzXr77bf13Xff6eyzz9bjjz+uyZMnKyEhQQcOHJC/v7+6deumzp0766GHHpLb7VZMTIyuuuoqNWjQQG+++aa+//57RUREKCIiQpdccon27dtnbXMeeeQRuVwu/fTTTxoyZIjy8vLkdDoVHR2tKVOmKCkpSZ07d9Yrr7yiJk2a6JprrlG3bt20cuVKxcTE6NVXX9W0adPUsmVLNWrUSG63W88884zmz5+vQ4cOKT4+Xjt27FD79u317bff6oYbblBQUJAuuOACxcfHKyEhQVu2bNFdd92lwsJCtW3bVmPHjlXdunWVnJys8PBwZWZmWjvw3i9HP/74Y2VkZGjw4ME6dOiQ9uzZo5SUFF111VVav3699uzZo27dumnPnj16+umndeWVV+r333/X4MGD5Xa75e/vr0WLFunll19WUVGRhg4dKrfbrY4dOyooKEhFRUWSjuzgb9q0SY899ph69+6t2NhYLVq0SJdddpni4+PVsWNHxcfHKykpSbt379aKFSu0Y8cOzZ8/X7GxsSooKFBOTo5atGihiy66SBs3btT333+vffv2aezYsUpPT1fnzp0VFRWl2bNnKz4+Xv/73/80aNAgffPNN3r77be1d+9e/fzzz3r//fcVExOjIUOGaNWqVfr555/1+OOPq0OHDurcubP+8Y9/WG2OGDFCCQkJSk1NVVRUlL799luNHTtWd999txo1aqS3335bH330kfLy8uTn56eOHTvK6XQqNTVVU6dO1ccff6zmzZurdevWatmypRo3bmx9MWaLQRnjx483kowk07dvXxMREWEiIiKMJOPn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rqSkJG3evNlaz721SrK2oV716tVT3bp1lZqaqvDwcGVmZio+Pl4ej0epqanavXu3kpKSVFJSokOHDlnb5+joaGv7e/jwYTkcDrlcLgUEBFjreW5urqKjo2WMsZZbcXGxtU3zeDzW56mfn5+1DTLGKCsrSwEBAdY217sfUPqvd1skHdk/yMvLU0ZGhrVv493Oel8j73L2/u/9HCi97ZWObOOKi4uVkpJifY7m5eVZr3ujRo0UFBRkfTZ4223RooU13wcOHFB+fr6aN2+uXbt2KTQ0VHXr1tWuXbt0+PBh6/kbNWqklJQUHT58WC1atFBgYKC2bt2qkJAQhYeHW9vqwsJC6/GWLVvUsmVLlZSUaMuWLdY2wLsOSUduoJGWlma9ztHR0dV6M43qdEaECgAAAAAnzmlz9ycAAAAANYNQAQAAAMAWQgUAAAAAWwgVAAAAAGwhVAAAAACwhVABAAAAwBZCBQCcZhwOh95///2aLuO01L17d9155501XQYA1DqECgA4BQwbNkwOh8P6YarY2Fj16tVLr776qvXDjl579+5Vnz59aqjSyps/f74iIyOrbTwAwMlHqACAU8Tll1+uvXv3ateuXfrss890ySWX6I477tCVV16p4uJia7y4uLgKf1UbAIATgVABAKeIgIAAxcXFqUGDBmrfvr3uu+8+ffDBB/rss880f/58a7zSpz8VFhZq7Nixio+PV2BgoBITEzVr1ixr3PT0dI0aNUqxsbEKDAxUq1at9PHHH1vD3333XbVs2VIBAQFKSkrSE0884VNTeadaRUZGWvXs2rVLDodD//73v3XJJZcoODhYbdu21bfffitJWrlypYYPH66MjAzrSMy0adOqtHzS09P197//XdHR0QoPD1ePHj20YcMGSdL27dvlcDi0detWn2mefPJJNWnSxHq8adMm9enTR6GhoYqNjdWNN96ogwcPVqkeADiTECoA4BTWo0cPtW3bVv/+97/LHT537lx9+OGHevvtt7Vt2zYtXLhQSUlJkiSPx6M+ffro66+/1oIFC7R582Y98sgj8vPzkyStXbtWAwcO1KBBg7Rx40ZNmzZNU6ZM8Qkwx+v+++/X+PHj9eOPP6pZs2a67rrrVFxcrIsuukhPPfWUwsPDtXfvXu3du1fjx4+v0rK49tprlZqaqs8++0xr165V+/btdemllyotLU3NmjVThw4dtHDhQp9pFi5cqOuvv17SkVDSo0cPtWvXTmvWrNGSJUu0f/9+DRw4sEr1AMCZxL+mCwAA2NO8eXP973//K3fYb7/9pqZNm6pLly5yOBxKTEy0hi1btkzff/+9tmzZombNmkmSGjdubA2fM2eOLr30Uk2ZMkWS1KxZM23evFmPPfaYhg0bVqkax48fr759+0qSpk+frpYtW2rnzp1q3ry5IiIi5HA4FBcXV6k2S1u1apW+//57paamWqd+Pf7443r//ff1zjvvaOTIkRo8eLCeffZZPfjgg5KOHL1Yu3atFixYIEl69tln1a5dO82cOdNq99VXX1VCQoK2b99uLSMAQFkcqQCAU5wxRg6Ho9xhw4YN048//qizzz5bt99+u7744gtr2I8//qiGDRtWuLO8ZcsWde7c2adf586dtWPHDpWUlFSqxjZt2lj/x8fHS5JSU1Mr1caxbNiwQdnZ2apbt65CQ0OtLiUlRT///LMkadCgQdq1a5e+++47SUeOUrRv317Nmze32vjyyy99pvcO87YBACgfRyoA4BS3ZcsWJScnlzusffv2SklJ0WeffaZly5Zp4MCB6tmzp9555x0FBQXZfm6HwyFjjE+/oqKiMuO5XC6faSSVuWuVHdnZ2YqPj9fKlSvLDPPeMSouLk49evTQokWLdOGFF2rRokUaPXq0Txv9+vXTo48+WqYNbxACAJSPUAEAp7AVK1Zo48aNGjduXIXjhIeH629/+5v+9re/acCAAbr88suVlpamNm3a6Pfff6/w1J4WLVro66+/9un39ddfq1mzZtZ1F9HR0dq7d681fMeOHcrNza3UPLjd7kof+Tha+/bttW/fPvn7+1vXjJRn8ODBmjhxoq677jr98ssvGjRokE8b7777rpKSkuTvz8cjAFQGpz8BwCmioKBA+/bt0549e7Ru3TrNnDlTV111la688koNGTKk3GnmzJmjN998U1u3btX27du1ePFixcXFKTIyUhdffLG6deum/v37a+nSpdYRjSVLlkiS7r77bi1fvlwPPvigtm/frtdff13PPvusz4XUPXr00LPPPqv169drzZo1uuWWW3yOShyPpKQkZWdna/ny5Tp48OAxQ0lJSYl+/PFHn27Lli3q2bOnOnXqpKuvvlpffPGFdu3apW+++Ub333+/1qxZY01/zTXXKCsrS6NHj9Yll1yi+vXrW8PGjBmjtLQ0XXfddfrhhx/0888/6/PPP9fw4cNthx4AON0RKgDgFLFkyRLFx8crKSlJl19+ub788kvNnTtXH3zwgXXk4GhhYWGaPXu2OnTooPPPP1+7du3Sp59+KqfzyOb/3Xff1fnnn6/rrrtO55xzjiZOnGjtQLdv315vv/223nrrLbVq1UpTp07VjBkzfC7SfuKJJ5SQkKCuXbvq+uuv1/jx4xUcHFyp+brooot0yy236G9/+5uio6M1e/bsCsfNzs5Wu3btfLp+/frJ4XDo008/Vbdu3TR8+HA1a9ZMgwYN0q+//qrY2Fif5dGvXz9t2LBBgwcP9mm7fv36+vrrr1VSUqLLLrtMrVu31p133qnIyEhreQEAyucwR58MCwAAAACVwFcvAAAAAGwhVAAAAACwhVABAAAAwBZCBQAAAABbCBUAAAAAbCFUAAAAALCFUAEAAADAFkIFAAAAAFsIFQAAAABsIVQAAAAAsIVQAQAAAMAWQgUAAAAAW/4fjbaENuIKN0QAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Order_Value_Group'] = pd.cut(\n",
        "    df['Order_Value'],\n",
        "    bins=[0, 500, 1000, 2000, 3000, float('inf')],\n",
        "    labels=['Under 500', '500-999', '1000-1999', '2000-2999', '3000+']\n",
        ")\n",
        "\n",
        "df[['Order_Value', 'Order_Value_Group']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "RcoUBKdYdrEn",
        "outputId": "f4b11342-0d1a-4841-b004-0315e1e1bb99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Order_Value Order_Value_Group\n",
              "0  2393.163468         2000-2999\n",
              "1  2618.347140         2000-2999\n",
              "2  2567.404800         2000-2999\n",
              "3  3603.672300             3000+\n",
              "4  4921.525630             3000+"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-780b4dd6-411d-4ec7-ae1c-74770d5b561b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Order_Value</th>\n",
              "      <th>Order_Value_Group</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2393.163468</td>\n",
              "      <td>2000-2999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2618.347140</td>\n",
              "      <td>2000-2999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2567.404800</td>\n",
              "      <td>2000-2999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3603.672300</td>\n",
              "      <td>3000+</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4921.525630</td>\n",
              "      <td>3000+</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-780b4dd6-411d-4ec7-ae1c-74770d5b561b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-780b4dd6-411d-4ec7-ae1c-74770d5b561b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-780b4dd6-411d-4ec7-ae1c-74770d5b561b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df[['Order_Value', 'Order_Value_Group']]\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"Order_Value\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1062.298902037851,\n        \"min\": 2393.163468,\n        \"max\": 4921.52563,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          2618.34714,\n          4921.52563,\n          2567.4048\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Value_Group\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"3000+\",\n          \"2000-2999\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "order_value_return_rate = (\n",
        "    df.groupby('Order_Value_Group', observed=True)['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(order_value_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-GmTUrrWd40L",
        "outputId": "920eecd0-bf62-4784-a47d-18917a34803f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Order_Value_Group\n",
            "Under 500    31.028369\n",
            "2000-2999    30.011587\n",
            "1000-1999    28.750982\n",
            "500-999      28.535980\n",
            "3000+        28.112450\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "order_value_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Order Value')\n",
        "plt.xlabel('Order Value Group')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "ujO6t41dd6nE",
        "outputId": "f445952e-1f85-420d-a233-1b70bc38f074"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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R3H58mXz0BVJatasmXr27Klbt27p22+/VWRkpC1KRCqyYsUKBQcH65NPPlHNmjXVsmVLNWzYUDt37lT79u116dIlSQxZQNLCw8PVunVrderUSevXr9e6deu0bt06rVixQqNHj9a6detsXSLsxMmTJ1W1alUVKVJEAwYMUL169TRq1Cj16tVLu3btsnV5sFMxMTHmn2NjY21YiX0jWMBq2bNn1507d3TkyBFJ//c/XIMGDdS8eXPNnTtXFy9etGWJSAWOHTumCxcuWLQVL15cvXr1UmxsrFq1aiVJDFlAkiIjI+Xg4KCmTZvKMAxFR0erSJEiKlKkiPbt26cvv/xSN2/etHWZsDHDMPTVV1+pVq1amjJliurUqaNPPvlEderU0a+//qoBAwZo9+7dti4TdmbixIlavny5oqKiJElOTk46d+6cvvnmGxtXZn94h0ayJXxTHB8fb5HWGzRooDJlyqh169a6dOmSnJyczNu7du2qTJkyafXq1TapGfYvLi5OklSxYkXFx8dr5cqVkh59q9ijRw8VKFBAX375pS5duqT9+/fbslTYsbt372rv3r26ePGiTCaTXF1dde/ePWXJkkWTJ0/Wzz//rMWLF9u6TNiYyWRSWFiYed7WvXv3JEnFihVTzZo1FRMTo6VLlyomJoZFI2B24MABLViwwPxZ5urVqwoICNAff/xh48rsD8ECyZKw+tPRo0fVuXNnBQcHa/Dgwfr+++8lSQsWLFDmzJlVtWpVnThxQk5OTpIeTY7LkCGDfH19bVk+7NC/u5IrVqyojBkzqn///ipRooRKlCihli1bqmvXripWrJiuXLmic+fO2aZY2L2CBQuqXbt26tGjh7744gstWrRIAQEByps3r9555x198MEH2rJlCx8YoXTp0mndunWKjIyUh4eHrl69qk8//VQdOnRQw4YNNWfOHN26dYtl02H+WzF37lwVKFBACxcu1KxZsxQQEKCWLVtq5syZNq7Q/jB5G8l27NgxBQYGKiQkRD4+Ptq3b58iIyNVr149jRs3TpcvX1bTpk114sQJ9e/fX1myZNHBgwf19ddf688//1TevHlt/RJgJ44ePaoJEybo3r17cnFxUZ8+fVS8eHFdvXpVO3bs0IULF5QzZ07Vr19f0qOJ3S1atNDMmTNVokQJm9YO+xAWFqbw8HBdu3ZNQUFBkqQjR45o9uzZ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UnRsBwcHtW3bVt9++61GjBihuXPnqmrVqsqTJ48kqV+/flq3bp0+//xz5cuXT+7u7mrcuPFjJ0Q7ODz6nuuf4erfE8fv3r2runXravz48YkenzVr1iSPmz9//kQBIFOmTMqUKZMyZ86caP+n+b06ODgkCoVJTXoHgJcdPRYAYGMZMmRQzZo19dVXXyVaaenq1atatGiRmjRpkmg+wD8VKlRIO3futGjbsWOHxf033nhDx48fV758+RLdEj7Yp0S7du108eJFff/991q5cqU6dOhg3vb777+rbdu2atCggYoWLSpfX1+dO3fuscdKCE1Xrlwxt/1zIndC/YcPH1auXLkS1f+4QNCsWTMdP35cq1atSvHrkx79Xvfv36979+5ZvDYHBwfz5O5MmTJZ1B0XF6dDhw4lOta//z127NihQoUKPVVdAGCPCBYAYAemTp2q6OhoBQcHa+vWrbp48aLWrFmjmjVrKnv27EmuzvRP77//vtasWaPPP/9cJ0+e1NSpU7VmzRqLfYYNG6b58+dr5MiROnz4sI4ePaqlS5dqyJAhT1Vz7ty5Va1aNb333ntydXW16AnJnz+/vv/+e+3bt0/79+9X8+bNFR8f/9hjubu7q1y5cvrkk0909OhRbdmyJVFd3bt3V3h4uJo1a6a//vpLp0+f1tq1a9WuXTvFxcUledymTZuqcePGatq0qUaNGqWdO3fq3Llz2rJli5YtWyZHR8cnvsYWLVrIzc1Nbdq00aFDh7Rp0yb17NlTrVq1UpYsWSRJ1apV0+rVq7V69WodO3ZMXbt21e3btxMd6/fff9enn36qEydOaNq0aQoNDVWvXr2e+PwAkJoQLADADuTPn1+7du1Snjx59O677ypv3rx67733VLVqVW3fvl3p06d/4uPLlSun2bNna/LkySpevLh+/fXXRB/Mg4OD9dNPP+nXX39V6dKlVa5cOU2cOFH+/v5PXXeHDh1069YtNW/e3GI41YQJE5QuXTqVL19edevWVXBwsN54440nHuubb75RbGysAgIC1Lt370SrWmXLlk2///674uLiVKtWLRUtWlS9e/dW2rRpH9vjYjKZtGzZMk2aNEk///yzqlevrtdee03t27eXn5+ftm3b9sSa0qRJo7Vr1yo8PFylS5dW48aNVb16dU2dOtW8T/v27dWmTRu1bt1aQUFBypMnj6pWrZroWB988IF27dqlkiVLasyYMZowYYKCg4Of+PwAkJqYjJTMFgQAACmWK1cu9e7dO9H1LgDgZUKPBQAAAACrESwAAAAAWI2hUAAAAACsRo8FAAAAAKsRLAAAAABYjWABAAAAwGoECwAAAABWI1gAAAAAsBrBAgAAAIDVCBYAAAAArEawAAAAAGA1ggUAAAAAq/0/SoeixEv3hlAAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "returned_df = df[df['Return_Status'] == 'Returned']\n",
        "\n",
        "return_reason_counts = returned_df['Return_Reason'].value_counts()\n",
        "\n",
        "print(return_reason_counts)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mOSwA94Fd8Wc",
        "outputId": "3aa8f4b9-2542-45eb-abcb-54a2f315062b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Return_Reason\n",
            "Defective       382\n",
            "Changed Mind    379\n",
            "Wrong Item      348\n",
            "Size Issue      341\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "return_reason_percentage = (\n",
        "    returned_df['Return_Reason']\n",
        "    .value_counts(normalize=True) * 100\n",
        ")\n",
        "\n",
        "print(return_reason_percentage)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qTxqpoB1eA5m",
        "outputId": "898bfc1e-4008-473b-8beb-3a2fa4b0cbb7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Return_Reason\n",
            "Defective       26.344828\n",
            "Changed Mind    26.137931\n",
            "Wrong Item      24.000000\n",
            "Size Issue      23.517241\n",
            "Name: proportion, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "return_reason_percentage.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Reasons Distribution')\n",
        "plt.xlabel('Return Reason')\n",
        "plt.ylabel('Percentage of Returned Orders (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "0krx3sl9eCz7",
        "outputId": "376e9d10-c4b1-4bda-b677-5c7d99968c6e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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atRIH3zwgdKnT69du3axZjTeGYkTJ5ajo6NcXV0lPV8utnDhwlq1apVKlSqlcePG6euvv1a5cuUk/d+8JIaR4G0yXrjhYr9+/VS+fHm5ubnp8uXLunjxoooXL24ZalK6dGm5ubnp4cOHkmTpqTC4aSNsIFGiRDp37pwqVqyoDh066KuvvlLGjBmj7dO1a1dFRESoV69ekqRu3brJ29tbjRs31tChQ5UnTx5blI44QrB4hyVKlEg3btxQ1apVVatWLY0aNUqSLHcOTpw4sZo1a6aAgAANGDBAhmFozpw56t+/vzJkyCCz2azkyZPb+FMAb8Z4xWIFLi4uCg4O1rFjx1SiRAlJzye15s+fX3ny5NGOHTtkMpmUO3duubm5sawy3roXz9uVK1dq9uzZqlatmvLly6e6deuqb9++Gj9+vAoXLixJcnV1lYuLy0tLIXPuwhaePXumQYMGqXnz5ho9erSlPTw8XHfv3lVgYKDy5cunHj16yDAM9evXT8HBwRo5cqQWL17McNN3AJcz3nGRkZHKmjWrQkNDtWvXLknPf+EkTpzY8ouoQ4cOyps3r/78809JUtasWeXq6kqogN2KWqxAer5kYUREhMLCwpQjRw716tVLXbp00Zo1a5Q4cWI5ODjIbDardOnS+vHHH7VmzRr9+uuvNv4EeB89evTIct7+8ccf2rJli7799ltVrlxZKVKkUJs2beTk5KTWrVtr4cKFWrFihVq2bClXV1dVr17dxtUDz3uF79y5E63XYcOGDerdu7fy58+v2rVrq3LlyjIMQz179tTQoUM1bdo0PXjwgFDxjmC52ffAxYsX1bVrVxmGoYEDB740zEOSKleurEyZMmnRokW2LBWIU8OHD9eqVauUJEkS1a5dW506dVLy5MnVrVs3TZs2Td26dVPatGm1ZcsW+fv768iRI6pevbrSp0+v+fPn27p8vEd27NihBg0a6Pz58woMDFSDBg105coVDR8+XF999ZVlv7/++ku//fabFi1apDx58sjNzU1r1qyRo6MjS8rC5gIDA1WyZEmVL19ePXv21IoVKzR//nwVKFBAFSpUULJkyTR69GjVqlVLkydPliQ9fvxYqVOntm3hiDMEi/fEi+Hi22+/VdmyZSU9v7L7zz//qH379mratKl8fX1fe78LIKF78dydP3++evbsqTFjxmjr1q26evWqvLy8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w0NFixZVt27ddOPGDZ07d86yfdeuXSpfvrycnZ3l6emprl27KiQkxLJ94cKFKl68uJInTy4PDw81b95c9+7ds2x//PixWrRoITc3Nzk7OytnzpyaO3euZfvJkydVpUoVOTs7K23atGrfvr2Cg4Mt21u1aqV69epp/PjxypAhg9KmTavOnTvHOlABwLuAYAEA75BTp05pz549SpIkiaVt9OjRWrBggWbMmKHTp0+re/fu+uyzz7R9+3Z5enpq+fLlkv6vt2DKlClWveeQIUNUv359nTx5Um3atJEkXb58WatWrdK6deu0bt06bd++XWPGjInxMQMCArRkyRJJsnyWy5cvq3r16mrYsKFOnDihX3/9Vbt27VKXLl0srwsPD9fw4cN1/PhxrVq1SlevXrUEJUn69ttvdebMGf355586e/aspk+frnTp0kmSQkJC5OPjo9SpU+vgwYNaunSpNm/eHO34krR161ZdvnxZW7du1fz58zVv3jzNmzfPqp8ZALyTDACA3fL19TUcHBwMV1dXw8nJyZBkJEqUyFi2bJlhGIbx7Nkzw8XFxdizZ0+017Vt29b49NNPDcMwjK1btxqSjMePH0fbx8vLy5g0aVK0tkKFChmDBw+2PJdkdOvWLdo+gwcPNlxcXIzAwEBL2zfffGOULFnytZ8jqgZXV1fD1dXVkGRIMurUqROt5vbt20d73c6dO41EiRIZT58+feVxDx48aEgygoKCDMMwjE8++cRo3br1K/edOXOmkTp1aiM4ONjS9vvvvxuJEiUy7ty5YxjG85+3l5eXERERYdmncePGRtOmTV/72QDgfZHYhpkGABAHKleurOnTpyskJESTJk1S4sSJ1bBhQ0nSpUuX9OTJE3388cfRXhMWFqYiRYrEyfsXL178pbYsWbIoefLklucZMmSINiTpdXbu3CkXFxft27dPo0aN0owZMyzbjh8/rhMnTmjx4sWWNsMwZDabdeXKFeXNm1eHDx/WkCFDdPz4cT1+/Fhms1mSdP36deXLl09ffvmlGjZsqCNHjqhatWqqV6+eypQpI0k6e/asChUqJFdXV8vxy5YtK7PZrPPnzyt9+vSSpPz588vBwSHaZ2OSOQBIBAsAsHOurq7KkSOHJGnOnDkqVKiQZs+erbZt21rmB/z+++/KlClTtNc5OTn953ETJUokwzCitb1qLsGLX8SjODo6RntuMpksX/L/S9asWZUqVSrlzp1b9+7dU9OmTbVjxw5JUnBwsDp06KCuXbu+9LoPPvjAMpTJx8dHixcvlpubm65fvy4fHx/LBPAaNWro2rVr+uOPP7Rp0yZVrVpVnTt31vjx4/9nbbH9bADwrmOOBQC8QxIlSqT+/ftr4MCBevr0qfLlyycnJyddv35dOXLkiPbw9PSU9H9zGCIjI6Mdy83NTbdv37Y8DwwM1JUrV97aZ+ncubNOnTqllStXSpKKFi2qM2fOvPQ5cuTIoSRJkujcuXN6+PChxowZo/LlyytPnjyv7CVxc3OTr6+vFi1apMmTJ2vmzJmSpLx58+r48ePRJoPv3r1biRIlUu7cud/OhwYAO0awAIB3TOPGjeXg4KAffvhByZMnV69evdS9e3fNnz9fly9f1pEjRzR16lTNnz9fkuTl5SWTyaR169bp/v37ll6OKlWqaOHChdq5c6dOnjwpX1/faEOA4puLi4vatWunwYMHyzAM9enTR3v27FGXLl107NgxXbx4UatXr7ZMrv7ggw+UJEkSTZ06VX///bfWrFmj4cOHRzvmoEGDtHr1al26dEmnT5/WunXrlDdvXklSixYtlDRpUvn6+urUqVPaunWrvvrqK33++eeWYVAAgNcjWADAOyZx4sTq0qWL/Pz8FBISouHDh+vbb7/V6NGjlTdvXlWvXl2///67smbNKknKlCmThg4dqr59+yp9+vSWL+r9+vVTxYoVVbt2bdWqVUv16tVT9uzZ3+pn6dKli86ePaulS5eqYMGC2r59uy5cuKDy5curSJEiGjRokDJmzCjpeU/EvHnztHTpUuXLl09jxox5aYhTkiRJ1K9fPxUsWFAVKlSQg4ODZfUpFxcXbdiwQY8ePdKHH36oRo0aqWrVqvr+++/f6mcGAHtlMv49gBYAAAAArESPBQAAAIBYI1gAAAAAiDWCBQAAAIBYI1gAAAAAiDWCBQAAAIBYI1gAAAAAiDWCBQAAAIBYI1gAAAAAiDWCBQAAAIBYI1gAAAAAiDWCBQAAAIBYI1gAAAAAiLX/B3WaHWTiYw/+AAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "monthly_return_rate = (\n",
        "    df.set_index('Order_Date')\n",
        "      .resample('M')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        ")\n",
        "\n",
        "print(monthly_return_rate.head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y8FhCW4OeEX0",
        "outputId": "7ba860ff-5ba5-4604-c860-1bf874fb3db1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Order_Date\n",
            "2022-01-31    27.272727\n",
            "2022-02-28    28.828829\n",
            "2022-03-31    21.568627\n",
            "2022-04-30    28.813559\n",
            "2022-05-31    25.619835\n",
            "2022-06-30    23.387097\n",
            "2022-07-31    29.752066\n",
            "2022-08-31    28.571429\n",
            "2022-09-30    26.363636\n",
            "2022-10-31    27.184466\n",
            "Freq: ME, Name: Return_Status, dtype: float64\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_6542/2047446845.py:3: FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.\n",
            "  .resample('M')['Return_Status']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12, 5))\n",
        "\n",
        "monthly_return_rate.plot()\n",
        "\n",
        "plt.title('Monthly Return Rate Trend')\n",
        "plt.xlabel('Month')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.grid(True)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 462
        },
        "id": "y0JVRy6leJ36",
        "outputId": "ba5204b5-ec7e-458c-ead8-462db6961959"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x500 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "location_return_rate = (\n",
        "    df.groupby('User_Location')['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(location_return_rate.head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hLIDUVMBeMRV",
        "outputId": "6df0ea18-eecf-49fe-b501-992d66ddcc45"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "User_Location\n",
            "City44    50.000000\n",
            "City85    43.902439\n",
            "City77    43.181818\n",
            "City55    42.000000\n",
            "City58    42.000000\n",
            "City5     41.666667\n",
            "City56    40.000000\n",
            "City90    39.622642\n",
            "City20    38.709677\n",
            "City62    38.461538\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "location_return_rate.head(10).plot(kind='bar')\n",
        "\n",
        "plt.title('Top 10 Locations by Return Rate')\n",
        "plt.xlabel('Location')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 607
        },
        "id": "a24ncyAxeVmr",
        "outputId": "af2a2e07-d961-41dd-9569-2d3e34270672"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAXRlJREFUeJzt3XmcjfX///HnGbPZZjDGMGGMfd/DIHvWyBqlskWEQtk+KUZFKypLdiWEhFRIQlnLmiVjlwwj2wwzzDDz/v3hN+frGDIz5jrHTI/77Ta3nPd1neu85uXqOM9zXdf7shljjAAAAAAAQJpzc3UBAAAAAABkVIRuAAAAAAAsQugGAAAAAMAihG4AAAAAACxC6AYAAAAAwCKEbgAAAAAALELoBgAAAADAIoRuAAAAAAAsQugGAAAAAMAihG4AAB5ihQoVUteuXV1dxl3Vq1dPZcuWdXUZAAA81AjdAPAfZbPZkvWzfv16y2uZMmWKOnTooIIFC8pms/1ryLx8+bJ69eolf39/Zc2aVfXr19fOnTuT9ToPa0jcvHmzRo0apcuXL7u6lIfSnfukj4+P6tatq++//z7V2xwzZoyWLVuWdkWmoVGjRjn8vh4eHipUqJBefvnlVO8j4eHhGjVqlHbv3p2mtQIA7s/d1QUAAFxj7ty5Do+/+OILrVmzJsl4qVKlLK/lvffe05UrV1StWjWdOXPmnuslJCSoRYsW2rNnjwYPHqzcuXNr8uTJqlevnnbs2KFixYpZXqsVNm/erNDQUHXt2lU5cuRwWBYWFiY3N74jf/zxx/X888/LGKOTJ09qypQpatmypVauXKkmTZqkeHtjxoxR+/bt1bp167QvNo1MmTJF2bJlU3R0tNauXatPP/1UO3fu1MaNG1O8rfDwcIWGhqpQoUKqWLFi2hcLALgnQjcA/Ec9++yzDo+3bt2qNWvWJBl3hg0bNtiPcmfLlu2e63399dfavHmzFi9erPbt20uSnnrqKRUvXlwjR47U/PnznVWy03h5ebm6hIdC8eLFHfbNdu3aqXTp0vr4449TFbqtkJCQoLi4OHl7e6fJ9tq3b6/cuXNLkl588UV16tRJCxcu1G+//aZq1aqlyWsAAKzHV+cAgHuKjo7Wq6++qgIFCsjLy0slSpTQhx9+KGOMw3o2m039+vXTvHnzVKJECXl7e6tKlSr65ZdfkvU6QUFBstls913v66+/VkBAgNq2bWsf8/f311NPPaXly5crNjY2Zb/gPUyePFllypSRl5eXAgMD1bdv37ue1rtt2zY1b95cOXPmVNasWVW+fHl9/PHH9uV//PGHunbtqsKFC8vb21t58+ZV9+7ddeHCBfs6o0aN0uDBgyVJwcHB9lOKT5w4Ienu13QfO3ZMHTp0UK5cuZQlSxbVqFEjyanW69evl81m06JFi/TOO+8of/788vb2VsOGDXXkyBGHdQ8fPqx27dopb9688vb2Vv78+dWpUydFRkYmq187duxQzZo1lTlzZgUHB+uzzz6zL7t69aqyZs2qV155Jcnz/v77b2XKlEljx45N1uvcrlSpUsqdO7eOHj3qMB4bG6uRI0eqaNGi8vLyUoECBTRkyBCHfcNmsyk6Olqff/65vd+JPe7atasKFSqU5PUST/m+3e37feL+smrVKs2ZM0c2m02bNm3SoEGD7JdCtGnTRv/880+Kf9dEjz32mCQ5/M4XL17Ua6+9pnLlyilbtmzy8fFRs2bNtGfPHvs669ev16OPPipJ6tatm/13njNnjn2dbdu2qWnTpvL19VWWLFlUt25dbdq0KdW1AgD+D0e6AQB3ZYxRq1attG7dOvXo0UMVK1bU6tWrNXjwYJ0+fVrjx493WH/Dhg1auHChXn75ZXl5eWny5Mlq2rSpfvvttzS7jnrXrl2qXLlyktOtq1WrpmnTpunQoUMqV67cA73GqFGjFBoaqkaNGqlPnz4KCwvTlClT9Pvvv2vTpk3y8PCQJK1Zs0ZPPPGE8uXLp1deeUV58+bVn3/+qe+++84eMNesWaNjx46pW7duyps3r/bv369p06Zp//792rp1q2w2m9q2batDhw5pwYIFGj9+vP3Ipr+//13ri4iIUM2aNRUTE6OXX35Zfn5++vzzz9WqVSt9/fXXatOmjcP67777rtzc3PTaa68pMjJS77//vjp37qxt27ZJkuLi4tSkSRPFxsaqf//+yps3r06fPq3vvvtOly9flq+v77/269KlS2revLmeeuopPf3001q0aJH69OkjT09Pde/eXdmyZVObNm20cOFCjRs3TpkyZbI/d8GCBTLGqHPnzin+e4qMjNSlS5dUpEgR+1hCQoJatWqljRs3qlevXipVqpT27t2r8ePH69ChQ/ZruOfOnasXXnhB1apVU69evSTJ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Z599prfffvtfnxceHq7o6GiHo92HDh2SJIdZwMuWLatKlSpp3rx5yp8/v/766y99+umnqapVunULrfHjx2vEiBFq06aNbDabihQpoj179qhhw4b37em9lufMmfOuM9Un95Rwq2TLlk0jR45Ut27dtGjRInXq1EnSrRn969evr5kzZzqsf/nyZXtgl+79+ybuyz4+PvfclwEAD4bTywEAd9W8eXPFx8dr4sSJDuPjx4+XzWZTs2bNHMa3bNnicA3pqVOntHz5cjVu3PieR/xSqn379oqIiNA333xjHzt//rwWL16sli1bPvA9rRs1aiRPT0998sknDkcjZ86cqcjISLVo0UKSVLlyZQUHB2vChAlJAlri8xJ/5zuPak6YMCHJ6yYG1ruFvTs1b95cv/32m7Zs2WIfi46O1rRp01SoUKF7Xl98L1FRUbp586bDWLly5eTm5pasW7DdvHlTU6dOtT+Oi4vT1KlT5e/v73CNvyQ999xz+vHHHzVhwgT5+fkl2YdSwt3dXa+++qr+/PNPLV++XNKtMwtOnz6t6dOnJ1n/2rVrio6Otj/OmjXrXftdpEgRRUZG6o8//rCPnTlzRkuXLk11rWmlc+fOyp8/v9577z37WKZMmZLsY4sXL9bp06cdxu61j1WpUkVFihTRhx9+qKtXryZ5zbS6NAQA/ss40g0AuKuWLVuqfv36ev3113XixAlVqFBBP/74o5YvX64BAwYkucVS2bJl1aRJE4dbhklSaGjofV9rxYoV9vsK37hxQ3/88Yf9CGurVq1Uvnx5SbdCd40aNdStWzcdOHBAuXPn1uTJkxUfH5+s15FuhYi7Hb0NDg5W586dNXz4cIWGhqpp06Zq1aqVwsLCNHnyZD366KP2Sb/c3Nw0ZcoUtWzZUhUrVlS3bt2UL18+HTx4UPv379fq1avl4+OjOnXq6P3339eNGzf0yCOP6Mcff9Tx48eTvHZiOH399dfVqVMneXh4qGXLlkmulZakYcOGacGCBWrWrJlefvll5cqVS59//rmOHz+uJUuWJLmd2v38/PPP6tevnzp06KDixYvr5s2bmjt3rjJlyqR27drd9/mBgYF67733dOLECRUvXlwLFy7U7t27NW3aNPvt1RI988wzGjJkiJYuXao+ffokWZ5SXbt21Ztvvqn33ntPrVu31nPPPadFixapd+/eWrdunWrV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KirN6gUAAAAAICVcFrpPnTqlV155RWvWrJG3t3eabXfs2LEKDQ1Ns+0BAACkV4WGfe/qElLlxLstXF0CAKQZl51evmPHDp07d06VK1eWu7u73N3dtWHDBn3yySdyd3dXQECA4uLidPnyZYfnRUREKG/evPfc7vDhwxUZGWn/OXXqlMW/CQAAAAAAd+eyI90NGzbU3r17Hca6deumkiVLaujQoSpQoIA8PDy0du1atWvXTpIUFhamv/76SyEhIffcrpeXl7y8vCytHQAAAACA5HBZ6M6ePbvKli3rMJY1a1b5+fnZx3v06KFBgwYpV65c8vHxUf/+/RUSEqIaNWq4omQAAADgnjidH8DduHQitfsZP3683Nzc1K5dO8XGxqpJkyaaPHmyq8sCAAAAACBZHqrQvX79eofH3t7emjRpkiZNmuSaggAAAAAAeAAuv083AAAAAAAZFaEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAizxUtwwDAAAAgOQoNOx7V5eQaifebeHqEuBEHOkGAAAAAMAiHOkGAAAAANxXej27wNVnFnCkGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAA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nz9fy5cvV/bs2e3Xafv6+ipz5szy9fVVjx49NGjQIOXKlUs+Pj7q37+/QkJCmLkcAAAAAPDQc2nonjJliiSpXr16DuOzZ89W165dJUnjx4+Xm5ub2rVrp9jYWDVp0kSTJ092cqUAAAAAAKScS0O3Mea+63h7e2vSpEmaNGmSEyoCAAAAACDtPDSzlwMAAAAAkNEQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsAihGwAAAAAAixC6AQAAAACwCKEbAAAAAACLELoBAAAAALAIoRsAAAAAAIsQugEAAAAAsIhLQ/cvv/yili1bKjAwUDabTcuWLXNYbozRm2++qXz58ilz5sxq1KiRDh8+7JpiAQAAAABIIZeG7ujoaFWoUEGTJk266/L3339fn3zyiT777DNt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uX777TcNGjRIxYsX1zfffMMR7zRw48YNHTlyRJLk7u6u8PBwNWnSRIsWLdL27ds1fvx49e7dm1O40ogxRvv379e7776rb775Rm3btpUkdezYUXFxcZo1a5YkcbQ7DV29elW//PKLJMnf318XL15Us2bNNGHCBC1cuFAvvPCChgwZoh07dri40owjISFBR44cUebMme1jv/zyi3744QdVq1ZNtWvX1tSpU11YYfoXFRWl0aNHq1ChQmrXrp3279+vxo0b66WXXlKHDh3UqVMnDR06VJK49jWNJX722L17t/LkySNJatKkiby9vVWzZk0FBASoY8eOmjFjhivLzFBu3LihsLAwh6N9hQoV0quvvqrQ0FANGDBAy5Ytc12BGUx8fLwOHjzo8FmkevXqeu211/T0009r+PDhWr9+vesKzGBiY2O1bds2PfHEE2rcuLFu3rwpSXrmmWeUPXt2Xbx40cUVJpOLQz+S6W7fxEdFRZnatWubixcvGmOMef31142Pj4/x9/c3f/31lzHGmJs3bzq1zozo0qVLZtSoUcZms5kcOXKYESNGmHPnzhljjPn1119Nq1atTPv27c3Vq1ddXGnGceTIEfufE/fhadOmmeDgYPPbb7+5qqwM69ChQ6ZPnz7G29vb+Pn5mREjRphTp04ZY26d6VG9enUzaNAgF1eZcVy4cME8+eSTpmbNmubTTz81DRs2NEWKFDFbt241GzduNB988IHJnj272bhxo6tLTdd27txpAgMDTa1atUypUqXMoEGDzJ9//mkOHjxoPvroI5MvXz4zceJEV5eZYU2ZMsVUrFjRjBgxwnTq1Mlcv37dGGPMlStXzOjRo01QUJAJCwtzcZXp152fC1977TVTs2ZNc+zYMYfxs2fPmm7dupmWLVuaqKgoZ5aYoT377LPm2WefNf/884/D+O7du02zZs1M3759TUJCAmfSpJFFixaZb775xmHs7NmzJleuXOb33393UVUpw+GidCJx1s/bj17fuHFDZ8+eVUREhCRp+fLlypkzpwoVKqSJEyfq+vXrzECcStevX7fPdJsjRw4NGDBAY8aMUePGjfXiiy/Kz89PklS7dm3Vr19fP/30k6KiolxZcrr3+eefa+DAgZKkIkWK2McT9+GqVasqNjZWv/32myQmVHtQBw4cUHR0tCSpWLFievXVV/XCCy+oefPm6t+/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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Price_Group'] = pd.cut(\n",
        "    df['Product_Price'],\n",
        "    bins=[0, 500, 1000, 2000, 3000, float('inf')],\n",
        "    labels=['Under 500', '500-999', '1000-1999', '2000-2999', '3000+']\n",
        ")\n",
        "\n",
        "df[['Product_Price', 'Price_Group']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "ZlHBIkgeeb2H",
        "outputId": "a024aeab-2d14-4099-ac6a-17ef871a1be3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Product_Price Price_Group\n",
              "0        1720.71   1000-1999\n",
              "1         744.06     500-999\n",
              "2         983.68     500-999\n",
              "3        1855.65   1000-1999\n",
              "4        1770.97   1000-1999"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-12b26ada-0569-4c93-8782-617ebabdc62e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Product_Price</th>\n",
              "      <th>Price_Group</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1720.71</td>\n",
              "      <td>1000-1999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>744.06</td>\n",
              "      <td>500-999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>983.68</td>\n",
              "      <td>500-999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1855.65</td>\n",
              "      <td>1000-1999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1770.97</td>\n",
              "      <td>1000-1999</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-12b26ada-0569-4c93-8782-617ebabdc62e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-12b26ada-0569-4c93-8782-617ebabdc62e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-12b26ada-0569-4c93-8782-617ebabdc62e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df[['Product_Price', 'Price_Group']]\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"Product_Price\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 512.4800221764748,\n        \"min\": 744.06,\n        \"max\": 1855.65,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          744.06,\n          1770.97,\n          983.68\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Price_Group\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"500-999\",\n          \"1000-1999\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "price_return_rate = (\n",
        "    df.groupby('Price_Group', observed=True)['Return_Status']\n",
        "      .apply(lambda x: (x == 'Returned').mean() * 100)\n",
        "      .sort_values(ascending=False)\n",
        ")\n",
        "\n",
        "print(price_return_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BfUfAMJkenfG",
        "outputId": "5b828954-4164-49a0-d725-7a84c3056109"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Price_Group\n",
            "1000-1999    29.889016\n",
            "Under 500    29.158700\n",
            "500-999      27.143922\n",
            "Name: Return_Status, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8, 5))\n",
        "\n",
        "price_return_rate.plot(kind='bar')\n",
        "\n",
        "plt.title('Return Rate by Product Price')\n",
        "plt.xlabel('Product Price Group')\n",
        "plt.ylabel('Return Rate (%)')\n",
        "plt.xticks(rotation=45)\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "N-2HHNwkepdL",
        "outputId": "0c3339e9-fa10-4308-a69e-b8cfca9436b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "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eTk4OFjW9+rVSz4+Pvrhhx9sUjOAB0wmk65cuSIPDw9JUnR0tCSpbNmyatCggeLj47VixQrFx8czXXQ2RbAAJJUoUUKdOnVS37599d///lfLli1ThQoVFBwcrFatWmnw4MHavHkzf+wAG0qa/enw4cPq0aOHGjVqpBEjRuirr76SJC1ZskS+vr6qU6eOjh07JgcHB0kPBonmzp1bfn5+tiwfgKScOXNq3bp1ioqKkpubmy5fvqzJkyerS5cuat68uT755BPdunWL6aKzKQZv45l05coV3bx5U1evXlWtWrUkSYcOHdKCBQu0bNky5cuXT02bNtXYsWMlST169NDJkye1fv16W5YNPPOOHDmikJAQhYaGysvLS3v27FFUVJReffVVTZgwQRcuXFDbtm117NgxDR06VHnz5tX+/fv18ccfa8eOHQoODrb1QwCeaZGRkapXr55OnjypChUqaNu2bWrXrp3mz5+v+Ph4BQQEaNmyZapXr56tS8VjcLB1AcCTtm/fPrVs2VJeXl46deqUChYsqBEjRujVV1/V1KlTFR4eLpPJpLx580p60Cf0/v37Kl++vMxms0wmE9+kADZgGIYWLVqkBg0aWLomnj9/XitWrNCHH36ouLg4TZkyRb/88ov69++vL7/8UtevX5efn5/Wr19PqACesKNHj+qzzz7TiRMnVLNmTZUvX17Vq1fX77//rgkTJsjZ2VmdOnVSu3btJEn79++Xp6en8uXLZ+PK8bgIFnimnD17Vs2aNVNYWJg6dOignDlz6qWXXlK3bt108OBBDRgwIFl3iRMnTmjhwoVatWqVtm3bxlzbgA2ZTCadOnVKd+7csSwrUKCAunTpIhcXF3344Yfy8/PT0KFDNX36dN24cUP29vays7OTp6enDSsHnj0HDx5UjRo1FBoaKk9PT33yyScym83q2bOnevXqpZEjRybb3jAMRUREyM3NTb6+vjaqGtbiUxKeKTt27JC/v78GDRqkAgUKyNvbW+PGjZMk/fjjj/rkk08sAz5v3bqladOmadWqVdq4caNKlixpy9KBZ05qPXXr1q2r27dva9++fZZlOXPmVOvWrdWsWTOtXr1aly9fliTlypVL3t7ehArgCbt7966GDh2qHj16aNmyZfr444+1ZMkSXb58WQMGDND48eOTbb9jxw699dZbmj17thYuXKg8efLYqHJY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hg0bpoiICFWvXl2ff/65cufOLUlatmyZ+vTpo6VLl+rll1+2caXIzggWsKn79++rQYMGun//vr7//nvlzp1bsbGxcnFx0eXLl1W5cmVNnz5dr732mq1LBZ5ZSd2ekro7HT9+XN9++61MJpMGDRoks9msOXPmaOnSpSpSpIhmzZolLy8vXbp0STly5JBhGPL29rb1wwCeeRcvXtSsWbNUv3591a1b1/LelqSiRYuqWbNm+uCDD2xcJbIzRuPgiTl27JjCw8PVqVMnTZ8+XcePH5eTk5NGjRols9msNm3a6ObNm5ZuTs7OznJzc7PMTgHgyUr63impy6KdnZ2OHj2qrl27atq0afLy8rIs7969u9q3b68TJ06oX79+unnzpvLlyycvLy9CBZBF+Pv7a9iwYapevbqkB10aDcPQjRs3LJOoANYgWOCJOHTokCpXrqx9+/bpzp07GjVqlHr27KklS5aobt26GjlypO7cuaOKFStq7dq12rhxo6ZMmaLbt2+rbNmyti4feCaZTCZduXJFZcqU0bfffitJypcvn6pUqSLDMPTDDz9YLrTl6OioHj16KCwsTDt37tTw4cOZThbIgjw9PS1djqUH7/MZM2bo+vXrqlatmg0rw9OArlDIdPfv31eXLl3k6uqq+fPnS5JOnDihd955R6dOnVLXrl3VvXt3HT58WOPGjdP69euVM2dOOTo6avHixXrhhRds/AiAZ9dff/2l4cOHa8OGDfr000/18ssv6+7du/rwww/1zTffqEGDBnrvvfcsH1QSEhL02WefqV69epbrWQDImlasWKGNGzcqIiJCGzZsoMUCViNY4Ilo2LChChcurHnz5ln6dJ49e1ajRo3S8ePH9Z///EehoaGSpCNHjli+UWEGGcD2Tp06pYkTJyoiIkJLlizRyy+/rDt37mjSpElav369atSooffffz/Zt6AAsr59+/ZpxIgRmjRpkkqVKmXrcvAUIFggUyUmJspsNqtHjx66c+eOli5dKicnJxmGITs7O506dUpvvvmmAgIC9MUXX0hSssFkAJ6cpMHZSZKmgJakkydPatKkSfrf//5nmTkmKVxs2rRJZcuW1bRp0wgXQDbz8GyMgLUYY4FMkZiYKEmyt7eXo6OjwsLCtGrVKs2bN08mk0l2dnZKTExUUFCQJkyYoC+//FIHDx6UxNV4AVuxs7PTuXPntHLlSkmSg4OD5b0cHBys8PBwtW7dWl27dtWGDRvk4eGh4cOHq0qVKjp+/Lhu375tw+oBPA5CBTISF8hDhjt27Ji+++47vfHGG8qXL58kqVatWpo0aZIGDhyoHDlyqGvXrrK3t5ckeXh4qHjx4nJzc7Nl2cAzLyEhQeHh4Tpy5Iji4+PVtm1b2dvbKzExUfb29goODtbAgQMVFRWl999/X2XLlpWPj4/GjRun6Oho+fj42PohAABsiGCBDHXixAmFhITo1q1bunHjhgYNGmQZJ9GrVy9FR0ere/fuOnPmjJo3b67AwEBFREQoPj6eYAHYmIODg8aOHashQ4Zo/vz5MpvNeuONN5KFi5IlS6ply5bq27evoqKi5OPjoxw5cihHjhy2Lh8AYGOMsUCGiY6O1ltvvSWz2axKlSqpb9++GjJkiN5++23LN5lms1lLly5VeHi47O3t5eHhoaioKH333XfM/gRkEadPn1a/fv107949devWTa+//rokKT4+Xo6Ojtq3b5/efPNNffXVVypSpIiNqwUAZBW0WCDD2NnZqUKFCsqdO7fatGmjPHnyqG3btpJkCRd2dnbq0KGDatasqbNnz+revXsqU6aM8ufPb+PqASQpXLiwZs6cqX79+mnBggW6f/++wsLCLBerXLZsmXLkyMGsbQCAZGixQIaKjo5O1qXpiy++0Ouvv67BgwcrPDxcefLkUUJCgi5evKiCBQvasFIA/+b06dMaPHiwLly4oBdffFFVq1bVL7/8ooiICK1bt46LVwIAkiFYIFMkJibKzs5OJpNJK1as0BtvvKEhQ4ZowIAB+vDDD3XmzBktXrxYOXLkYBYoIAs7f/68PvnkE3311Veyt7dXQECAxo8fz5z3AIAUCBbINIZhWK5X8cUXX6h9+/YKCgrSyZMn9ccff6h8+fK2LhFAGpnNZsXExMje3l4uLi62LgcAkAURLJCpkl5eJpNJ9erV0549e7Rp0yaVKVPGxpUBSCsuWgkASAsGbyNTmUwmJSYm6u2339bGjRu1Z88eQgWQzRAqAABpwZW38USUKlVKu3fvZrAnAADAU4quUHgi6EoBAADwdKPFAk8EoQIAAODpRrAAAAAAYDWCBQAAAACrESwAAAAAWI1gAQAAAMBqBAsAAAAAViNYAAAAALAawQIAnnIdO3ZUs2bNbF1GmmW3egEADxAsAMAGOnbsKJPJJJPJJCcnJxUpUkRjx45VQkKCrUv7V4sWLZK3t3eatkt6jHZ2dipQoIA6deqkq1ev/uN+06dP16JFizKm2H+wcuVK1a1bVzlz5pSrq6uKFy+uzp07688//8z0cwPA04hgAQA20rhxY126dEnHjx/X4MGDNXr0aH3wwQepbnv//v0nXF3G8PT01KVLl3T+/HktWLBAP/30k9q3b5/qtomJiTKbzfLy8kpTcLFGeHi42rRpo/Lly+vbb7/V0aNHtXz5cgUFBWn48OGP3C+7/h4A4EkgWACAjTg7O8vPz0+BgYHq1auX6tevr2+//VbS/3UHev/99+Xv76/ixYtLkvbv36+6devK1dVVuXPnVvfu3XX37l3LMRMTEzVo0CB5e3srd+7cGjp0qAzDSHbeQoUKadq0acmWlS9fXqNHj7bcv337tnr06KG8efPKxcVFpUuX1vfff69NmzapU6dOioyMtLRGPLzf35lMJvn5+cnf31+hoaF66623tH79esXExFhaPr799ls999xzcnZ21tmzZ1N0hTKbzZo8ebKKFCkiZ2dnFSxYUO+//75l/blz59S6dWt5e3srV65catq0qf76669H1vT7779r8uTJmjJliqZMmaIaNWqoYMGCqlChgt555x399NNPlm1Hjx6t8uXL6+OPP1bhwoXl4uIiSTp79qyaNm0qd3d3eXp6qnXr1rpy5Yplv9S6cw0YMEC1a9e23K9du7b69u2rvn37ysvLS3ny5NHIkSNT/L4AILsgWABAFuHq6prsG/ENGzbo6NGjWrdunb7//ntFR0erUaNGypkzp/744w9FRERo/fr16tu3r2Wf//73v1q0aJE+/fRTbd26VTdv3tSqVavSVYfZbFZoaKh+/fVXLV26VIcOHdLEiRNlb2+vqlWratq0aZaWiEuXLmnIkCHpeoxms9nS5evevXuaNGmSPv74Yx08eFC+vr4p9hk+fLgmTpyokSNH6tChQ1q+fLny5s0rSYqPj1ejRo3k4eGhX375Rb/++qvc3d3VuHHjR7YufP7553J3d1fv3r1TXW8ymZLdP3HihFauXKmvvvpKe/bskdlsVtOmTXXz5k1t3rxZ69at06lTp9SmTZs0Pw9JPvvsMzk4OGjHjh2aPn26pkyZoo8//jjdxwGArMDB1gUAwLPOMAxt2LBBa9asUb9+/SzL3dzc9PHHH8vJyUmStGDBAsXGxmrx4sVyc3OTJM2aNUuvvPKKJk2apLx582ratGkaPny4mjdvLkmaO3eu1qxZk6561q9frx07dujw4cMqVqyYJCkoKMiy3svLy9ISkR7Hjx/X3LlzVbFiRXl4eEh6EAw++ugjlStXLtV97ty5o+nTp2vWrFkKCwuTJAUHB6t69eqSpC+++EJms1kff/yxJRAsXLhQ3t7e2rRpkxo2bJjimMeOHVNQUJAcHP7vv8ApU6bo3Xfftdy/cOGCvLy8JD3o/rR48WL5+PhIktatW6f9+/fr9OnTCggIkCQtXrxYpUqV0h9//KFKlSql+TkJCAjQ1KlTZTKZVLx4ce3fv19Tp05Vt27d0nwMAMgqaLEAABv5/vvv5e7uLhcXF4WGhqpNmzbJuhWVKVPGEiok6fDhwypXrpwlVEhStWrVZDabdfToUUVGRurSpUuqUqWKZb2Dg4MqVqyYrrr27NmjAgUKWEKFNSIjI+Xu7q4cOXKoePHiyps3r5YtW2ZZ7+TkpLJlyz5y/8OHDysuLk716tVLdf3evXt14sQJeXh4yN3dXe7u7sqVK5diY2N18uTJNNfZuXNn7dmzR/PmzVN0dHSy7kiBgYGWUJFUU0BAgCVUSNJzzz0nb29vHT58OM3nlKQXX3wxWQtJSEiIjh8/rsTExHQdBwCyAlosAMBG6tSpozlz5sjJyUn+/v7JvkGXlCxAZCQ7O7sU/fjj4+MtP7u6umbYuTw8PLR7927Z2dkpX758KY7t6uqaouvR39f/k7t376pChQrJwkqSh8PAw4oWLaqtW7cqPj5ejo6OkiRvb295e3vr/PnzKbZ/nN/Dvz3HAPA0osUCAGzEzc1NRYoUUcGCBVOEitSULFlSe/fuVXR0tGXZr7/+Kjs7OxUvXlxeXl7Kly+ftm/fblmfkJCgXbt2JTuOj4+PLl26ZLkfFRWl06dPW+6XLVtW58+f17Fjx1Ktw8nJKc3fqNvZ2alIkSIKCgp6rMBStGhRubq6asOGDamuf+GFF3T8+HH5+vqqSJEiyW5JXZn+7vXXX9fdu3f10Ucfpbse6cHv4dy5czp37pxl2aFDh3T79m0999xzklI+x9KDlqC/e/h3JT0YWF60aFHZ29s/Vm0AYEsECwDIJtq1aycXFxeFhYXpwIED2rhxo/r166f27dtbBjP3799fEydO1Ndff60jR46od+/eun37drLj1K1bV0uWLNEvv/yi/fv3KywsLNkH2Vq1aqlmzZpq0aKF1q1bp9OnT+unn37S6tWrJT2YVeru3bvasGGDrl+/rnv37mXaY3ZxcVF4eLiGDh2qxYsX6+TJk/r999/1ySefWJ6TPHnyqGnTpvrll190+vRpbdq0SW+99VaqrQ/Sg+5GgwcP1uDBgzVo0CBt3bpVZ86csRw36bobj1K/fn2VKVNG7dq10+7du7Vjxw516NBBtWrVsnQ7q1u3rnbu3KnFixfr+PHjGjVqlA4cOJDiWGfPntWgQYN09OhRff7555o5c6b69++fAc8cADx5BAsAyCZy5MihNWvW6ObNm6pUqZJatmypevXqadasWZZtBg8erPbt2yssLEwhISHy8PDQa6+9luw4w4cPV61atfTyyy+rSZMmatasmYKDg5Nts3LlSlWqVEmvv/66nnvuOQ0dOtTSSlG1alX17NlTbdq0kY+PjyZPnpypj3vkyJEaPHiw3n33XZUsWVJt2rSxXGQvR44c2rJliwoWLKjmzZurZMmS6tKli2JjY+Xp6fnIY3744Ydavny5/vzzT7388ssqWrSoWrVqJbPZrG3btv3jviaTSd98841y5sypmjVrqn79+goKCtIXX3xh2aZRo0YaOXKkhg4dqkqVKunOnTvq0KFDimN16NBBMTExqly5svr06aP+/fure/fuVjxbAGA7JoMJswEAeOJq166t8uXLp7imCABkV7RYAAAAALAawQIAAACA1egKBQAAAMBqtFgAAAAAsBrBAgAAAIDVCBYAAAAArEawAAAAAGA1ggUAAAAAqxEsAAAAAFiNYAEAAADAagQLAAAAAFYjWAAAAACw2v8D0Kjgh0UF7LYAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numeric_cols = [\n",
        "    'Product_Price',\n",
        "    'Order_Quantity',\n",
        "    'Discount_Applied',\n",
        "    'User_Age',\n",
        "    'Days_to_Return',\n",
        "    'Order_Value',\n",
        "    'Return_Cost',\n",
        "    'Profit_Loss',\n",
        "    'CO2_Emissions',\n",
        "    'Packaging_Waste',\n",
        "    'CO2_Saved',\n",
        "    'Waste_Avoided'\n",
        "]\n",
        "\n",
        "correlation_matrix = df[numeric_cols].corr()\n",
        "\n",
        "print(correlation_matrix)"
      ],
      "metadata": {
        "id": "LZfmlKsfesMy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "db8a7827-9d26-4663-b511-e79f1016040c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                  Product_Price  Order_Quantity  Discount_Applied  User_Age  \\\n",
            "Product_Price          1.000000       -0.005529         -0.003267 -0.017160   \n",
            "Order_Quantity        -0.005529        1.000000          0.001190 -0.004158   \n",
            "Discount_Applied      -0.003267        0.001190          1.000000 -0.044766   \n",
            "User_Age              -0.017160       -0.004158         -0.044766  1.000000   \n",
            "Days_to_Return         0.013576       -0.002306          0.065631  0.003330   \n",
            "Order_Value            0.662521        0.600828         -0.252510 -0.008894   \n",
            "Return_Cost            0.009355       -0.008031          0.079042 -0.004605   \n",
            "Profit_Loss            0.660758        0.600045         -0.255916 -0.008650   \n",
            "CO2_Emissions          0.003270       -0.014617          0.013055  0.000008   \n",
            "Packaging_Waste       -0.005529        1.000000          0.001190 -0.004158   \n",
            "CO2_Saved             -0.006305       -0.005549         -0.065503  0.008011   \n",
            "Waste_Avoided         -0.013687        0.562056         -0.052890  0.007210   \n",
            "\n",
            "                  Days_to_Return  Order_Value  Return_Cost  Profit_Loss  \\\n",
            "Product_Price           0.013576     0.662521     0.009355     0.660758   \n",
            "Order_Quantity         -0.002306     0.600828    -0.008031     0.600045   \n",
            "Discount_Applied        0.065631    -0.252510     0.079042    -0.255916   \n",
            "User_Age                0.003330    -0.008894    -0.004605    -0.008650   \n",
            "Days_to_Return          1.000000    -0.008962     0.859732    -0.051388   \n",
            "Order_Value            -0.008962     1.000000    -0.015076     0.998781   \n",
            "Return_Cost             0.859732    -0.015076     1.000000    -0.064414   \n",
            "Profit_Loss            -0.051388     0.998781    -0.064414     1.000000   \n",
            "CO2_Emissions           0.001656    -0.008867    -0.008212    -0.008444   \n",
            "Packaging_Waste        -0.002306     0.600828    -0.008031     0.600045   \n",
            "CO2_Saved              -0.766707     0.006443    -0.891798     0.050457   \n",
            "Waste_Avoided          -0.648590     0.345192    -0.754409     0.381758   \n",
            "\n",
            "                  CO2_Emissions  Packaging_Waste  CO2_Saved  Waste_Avoided  \n",
            "Product_Price          0.003270        -0.005529  -0.006305      -0.013687  \n",
            "Order_Quantity        -0.014617         1.000000  -0.005549       0.562056  \n",
            "Discount_Applied       0.013055         0.001190  -0.065503      -0.052890  \n",
            "User_Age               0.000008        -0.004158   0.008011       0.007210  \n",
            "Days_to_Return         0.001656        -0.002306  -0.766707      -0.648590  \n",
            "Order_Value           -0.008867         0.600828   0.006443       0.345192  \n",
            "Return_Cost           -0.008212        -0.008031  -0.891798      -0.754409  \n",
            "Profit_Loss           -0.008444         0.600045   0.050457       0.381758  \n",
            "CO2_Emissions          1.000000        -0.014617   0.388659      -0.012155  \n",
            "Packaging_Waste       -0.014617         1.000000  -0.005549       0.562056  \n",
            "CO2_Saved              0.388659        -0.005549   1.000000       0.662931  \n",
            "Waste_Avoided         -0.012155         0.562056   0.662931       1.000000  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12, 8))\n",
        "\n",
        "sns.heatmap(\n",
        "    correlation_matrix,\n",
        "    annot=True,\n",
        "    fmt='.2f',\n",
        "    cmap='coolwarm'\n",
        ")\n",
        "\n",
        "plt.title('Correlation Matrix of Numerical Variables')\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 782
        },
        "id": "GJ3XNS33bQj2",
        "outputId": "63ee68a6-629a-4604-dba7-1d351f1daa54"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x800 with 2 Axes>"
            ],
            "image/png": "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6BAAoGrVqqhcuTKWLFkCAJDJZLCxscFvv/2G0aNH50na2cOFiIiIiIiIiPJUYmIioqOjFZbExES17PvixYuoX7++wrpGjRrh4sWLAICkpCRcu3ZNIYxYLEb9+vXlYfKCdp7tmf4v7ddxK+gkaCT7+6cKOgkaRwR2nstKxjZuJdqilIJOgkYyXzOuoJOgccJ7/FnQSdA4Rdf8UdBJ0EisK8pkAu8/lDsCRAWdBI1TxtmyoJOgVgX5/9zVPzrD399fYd3EiRMxadKkb973u3fvUKJECYV1JUqUQHR0ND5+/IjIyEikpqaqDPPgwYNvPn522OBCRERERERERHlqzJgxGDZsmMI6iURSQKnJH2xwISIiIiIiIqI8JZFI8qyBxdLSEqGhoQrrQkNDYWxsDH19fWhpaUFLS0tlGEvLvOvFxP6FRERERERERIWASEdUYEte8vHxwfHjxxXWHT16FD4+PgAAXV1dVKxYUSGMTCbD8ePH5WHyAhtciIiIiIiIiEhjxMbGIigoCEFBQQDSpn0OCgrCy5cvAaS9nuTr6ysP37dvXzx9+hSjRo3CgwcPsGzZMvz7778YOnSoPMywYcOwatUqrF27Fvfv30e/fv0QFxcHPz+/PMsHXykiIiIiIiIiKgTE2t/HwMj//fcf6tSpI/+cPvZLt27dEBgYiJCQEHnjCwA4ODhg//79GDp0KBYuXIhSpUrh77//RqNGjeRhOnbsiA8fPmDChAl49+4dvLy8cOjQIaWBdNWJDS5EREREREREpDFq164NQch+1tPAwECVcW7cuJHjfgcOHIiBAwd+a/Jyja8UERERERERERGpGXu4EBERERERERUCIh32uchPLG0iIiIiIiIiIjVjDxciIiIiIiKiQuB7GTT3/wV7uBARERERERERqRl7uBAREREREREVAiId9nDJT+zhQkRERERERESkZmxwISIiIiIiIiJSM75SRERERERERFQIcNDc/MUeLkREREREREREasYeLkRERERERESFAAfNzV/s4UJEREREREREpGaFvsGle/fuaNWqVUEn46uIRCLs2rWroJNBRERERERERFlo7CtF3bt3x9q1awEAOjo6sLW1ha+vL8aOHQttbY1NNgIDAzFkyBBIpdJcx6lduzZOnz4NAJBIJHB0dMTAgQPRv3//HOOFhITAzMzsW5KrEcxrVoLj8J4w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qNWLX1sV2LEDrL2UxgidOHEiJk2apBT27du3KFmyJC5cuKAwYc6oUaNw+vRppSFHsurTpw8uXryIW7du5Rju6dOncHJywrFjx1CvXr3cZyaXvp8RczSEvb09Tp06BXd3d6UxWjRdfHw8njx5ghkzZqBPnz7f3S/4RERERERE9H1SNUbomDFjVIa1sLCAlpYWQkMVB0cODQ2FpaVljseJi4vD5s2b0bNnz8+mydHRERYWFnj8+HHuM/IFCnWDS9++fRWmkc689O3bN9t4Dg4OmDRpEipWrJiPqf12s2bNgru7OywtLbOt2ERERERERETqpmqM0OxmCNLV1UXFihVx/Phx+TqZTIbjx48r9HhRZevWrUhMTMTPP//82TS9fv0a4eHhsLKy+mzYr5FvY7hoosmTJ2c7hoqxsbHK9d+zSZMmqeyuRURERERERP//vqdpoYcNG4Zu3bqhUqVKqFKlChYsWIC4uDj4+fkBAHx9fVGyZElMn674Kvbq1avRqlUr+QQ36WJjY+Hv74+2bdvC0tIST548wahRo+Ds7IxGjRrlSR4KdYNL8eLFVc7fTUREREREREQFp2PHjvjw4QMmTJiAd+/ewcvLC4cOHZIPpPvy5UuIszQgBQcH49y5czhy5IjS/rS0tHDr1i2sXbsWUqkU1tbWaNiwIaZMmZJtT5tvVagbXIiIiIiIiIgKiy+dnrmgDRw4EAMHDlS57dSpU0rr3NzckN28QPr6+jh8+LA6k/dZ309/IiIiIiIiIiKi7wQbXIiIiIiIiIiI1IyvFBEREREREREVAt/ToLn/D1jaRERERERERERqxh4uRERERERERIWB6PsaNPd7xx4uRERERERERERqxh4uRERERERERIXA9zYt9PeOPVyIiIiIiIiIiNSMDS5ERERERERERGrGV4qIiIiIiIiICgFOC52/WNpERERERERERGrGHi5EREREREREhQAHzc1f7OFCRERERERERKRmbHAhIiIiIiIiIlIzvlJEREREREREVAhw0Nz8JRIEQSjoRND3497jtwWdBPpOPPOoU9BJ0DjW984XdBI0jqlYWtBJ0EjXwhwLOgkap3LRRwWdBI1zNdyloJOgkcpY8FklK5nAf7Cyik/VL+gkaCSxSFbQSdA43q5FCzoJavVu5M8FdmzL2RsK7NgFhT1ciIiIiIiIiAoBDpqbv9jc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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Return_Flag'] = df['Return_Status'].map({\n",
        "    'Not Returned': 0,\n",
        "    'Returned': 1\n",
        "})\n",
        "\n",
        "df[['Return_Status', 'Return_Flag']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "AY320uG-blT3",
        "outputId": "e20ae6f9-f2a2-4d14-8a52-34bd9749c542"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "  Return_Status  Return_Flag\n",
              "0  Not Returned            0\n",
              "1      Returned            1\n",
              "2  Not Returned            0\n",
              "3  Not Returned            0\n",
              "4      Returned            1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bddb60ed-e10e-40a0-b35c-acc031d76d42\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Return_Status</th>\n",
              "      <th>Return_Flag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Not Returned</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Returned</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Not Returned</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Not Returned</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Returned</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bddb60ed-e10e-40a0-b35c-acc031d76d42')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-bddb60ed-e10e-40a0-b35c-acc031d76d42 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-bddb60ed-e10e-40a0-b35c-acc031d76d42');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df[['Return_Status', 'Return_Flag']]\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"Return_Status\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Returned\",\n          \"Not Returned\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Return_Flag\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Order_Year'] = df['Order_Date'].dt.year\n",
        "df['Order_Month'] = df['Order_Date'].dt.month\n",
        "\n",
        "df['High_Discount'] = (df['Discount_Applied'] >= 0.20).astype(int)\n",
        "\n",
        "df[['Order_Year', 'Order_Month', 'High_Discount']].head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "_vSn0NOibsGB",
        "outputId": "7e4e7bcf-1bc7-471f-ff2c-d305038a3a40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Order_Year  Order_Month  High_Discount\n",
              "0        2022            1              1\n",
              "1        2022            1              1\n",
              "2        2025            3              1\n",
              "3        2024           11              1\n",
              "4        2023            6              1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-977c4909-0b51-4231-86c6-c3c1cfe706a4\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Order_Year</th>\n",
              "      <th>Order_Month</th>\n",
              "      <th>High_Discount</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2022</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2022</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2025</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2024</td>\n",
              "      <td>11</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2023</td>\n",
              "      <td>6</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-977c4909-0b51-4231-86c6-c3c1cfe706a4')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-977c4909-0b51-4231-86c6-c3c1cfe706a4 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-977c4909-0b51-4231-86c6-c3c1cfe706a4');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df[['Order_Year', 'Order_Month', 'High_Discount']]\",\n  \"rows\": 5,\n  \"fields\": [\n    {\n      \"column\": \"Order_Year\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2025,\n          2023,\n          2022\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Month\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          3,\n          6,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High_Discount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 1,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df['Return_Flag'].value_counts())\n",
        "print()\n",
        "print(df['Return_Flag'].value_counts(normalize=True) * 100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hk718jbKburZ",
        "outputId": "3609535c-0bfc-46a2-fa10-f51d63607deb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Return_Flag\n",
            "0    3550\n",
            "1    1450\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Return_Flag\n",
            "0    71.0\n",
            "1    29.0\n",
            "Name: proportion, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "features = [\n",
        "    'Product_Price',\n",
        "    'Order_Quantity',\n",
        "    'Discount_Applied',\n",
        "    'User_Age',\n",
        "    'Days_to_Return',\n",
        "    'Order_Value',\n",
        "    'Return_Cost',\n",
        "    'Profit_Loss',\n",
        "    'CO2_Emissions',\n",
        "    'Packaging_Waste',\n",
        "    'Order_Year',\n",
        "    'Order_Month',\n",
        "    'High_Discount'\n",
        "]\n",
        "\n",
        "X = df[features]\n",
        "y = df['Return_Flag']\n",
        "\n",
        "print(\"X shape:\", X.shape)\n",
        "print(\"y shape:\", y.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_hFT7UCdbxY7",
        "outputId": "2a044471-55c1-4aba-ea5a-d69b72dfd0b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "X shape: (5000, 13)\n",
            "y shape: (5000,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size=0.20,\n",
        "    random_state=42,\n",
        "    stratify=y\n",
        ")\n",
        "\n",
        "print(\"Training data:\", X_train.shape)\n",
        "print(\"Testing data:\", X_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jw3Wvvirb5EN",
        "outputId": "39b08350-3efc-4981-8b0e-55f613f552ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training data: (4000, 13)\n",
            "Testing data: (1000, 13)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "scaler = StandardScaler()\n",
        "\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)\n",
        "\n",
        "print(\"Training data shape:\", X_train_scaled.shape)\n",
        "print(\"Testing data shape:\", X_test_scaled.shape)"
      ],
      "metadata": {
        "id": "LfP8cb7LcGTf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2d77e9db-86d9-47e3-ccef-4d36d87a2dbf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training data shape: (4000, 13)\n",
            "Testing data shape: (1000, 13)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "scaler.fit_transform(X_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8GPUhM5ElnJa",
        "outputId": "20e87d93-e817-4044-93b0-3f69c8b91ff9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-3.14010355e-01, -1.42558956e+00,  1.71502920e+00, ...,\n",
              "         5.86098959e-01,  2.46149464e-01,  6.72334852e-02],\n",
              "       [ 3.37949362e-01,  7.14132108e-01, -4.67878791e-01, ...,\n",
              "         5.86098959e-01, -9.37617120e-01,  6.72334852e-02],\n",
              "       [-2.02594644e-01, -1.42558956e+00, -4.97011977e-01, ...,\n",
              "         5.86098959e-01, -4.97921819e-02,  6.72334852e-02],\n",
              "       ...,\n",
              "       [ 9.20758964e-02, -1.42558956e+00, -1.62696340e+00, ...,\n",
              "         5.86098959e-01,  5.42091110e-01,  6.72334852e-02],\n",
              "       [-1.39165214e+00, -1.42558956e+00,  7.39761126e-01, ...,\n",
              "        -3.47551314e-01, -1.52950041e+00,  6.72334852e-02],\n",
              "       [ 1.14178127e+00,  8.91550696e-04,  6.01725317e-01, ...,\n",
              "         5.86098959e-01, -4.97921819e-02,  6.72334852e-02]])"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "scaler.transform(X_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YQpQvncbmFaC",
        "outputId": "61ecf7e5-5d5d-4375-d7ec-caae163c8d6a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[-8.23849966e-01, -7.12349006e-01, -9.81177779e-01, ...,\n",
              "        -3.47551314e-01,  1.13397440e+00,  6.72334852e-02],\n",
              "       [ 2.23998326e-02, -1.42558956e+00, -6.82909448e-01, ...,\n",
              "        -3.47551314e-01, -1.52950041e+00,  6.72334852e-02],\n",
              "       [ 5.67691564e-01,  8.91550696e-04, -1.42511204e+00, ...,\n",
              "        -3.47551314e-01, -3.45733828e-01,  6.72334852e-02],\n",
              "       ...,\n",
              "       [-1.18238565e+00,  1.42737266e+00,  4.77562454e-01, ...,\n",
              "         5.86098959e-01,  8.38032756e-01,  6.72334852e-02],\n",
              "       [-8.52580266e-02,  8.91550696e-04,  2.56288971e-01, ...,\n",
              "         5.86098959e-01,  5.42091110e-01,  6.72334852e-02],\n",
              "       [-7.86253121e-01, -1.42558956e+00,  1.49444937e+00, ...,\n",
              "        -1.28120159e+00,  1.72585769e+00,  6.72334852e-02]])"
            ]
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "model = LogisticRegression(random_state=42)\n",
        "\n",
        "model.fit(X_train_scaled, y_train)\n",
        "\n",
        "print(\"Logistic Regression model trained successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7oO1UyGnmH-e",
        "outputId": "1b67e467-10f6-4bb2-ec03-9cd025ca977a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Logistic Regression model trained successfully.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test_scaled)\n",
        "\n",
        "print(\"Predictions:\")\n",
        "print(y_pred[:20])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TNdiLQHHmK2F",
        "outputId": "ca17dd09-e7b5-4240-bbea-7581079346e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predictions:\n",
            "[1 0 1 0 0 0 0 1 0 1 1 0 0 1 0 0 1 0 0 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_probability = model.predict_proba(X_test_scaled)[:, 1]\n",
        "\n",
        "print(\"Return probabilities:\")\n",
        "print(y_pred_probability[:20])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rKP_j3j-mTEF",
        "outputId": "3a67d8bf-7927-4efa-a511-c3f43e457390"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Return probabilities:\n",
            "[9.99959592e-01 8.30132536e-04 9.99982864e-01 9.34221311e-04\n",
            " 9.40185695e-04 8.48631583e-04 7.66616394e-04 9.99384148e-01\n",
            " 7.18300323e-04 9.89758735e-01 9.93124788e-01 8.05450919e-04\n",
            " 8.62193488e-04 9.99981722e-01 8.85283905e-04 7.91716537e-04\n",
            " 9.99975329e-01 8.51137481e-04 9.73350699e-04 6.60705998e-04]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score, precision_score, recall_score\n",
        "\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "precision = precision_score(y_test, y_pred)\n",
        "recall = recall_score(y_test, y_pred)\n",
        "\n",
        "print(\"Accuracy :\", round(accuracy * 100, 2), \"%\")\n",
        "print(\"Precision:\", round(precision * 100, 2), \"%\")\n",
        "print(\"Recall   :\", round(recall * 100, 2), \"%\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZOhUU8XymWCP",
        "outputId": "e9157b37-fbf4-4272-bc74-8e891b4e2155"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy : 100.0 %\n",
            "Precision: 100.0 %\n",
            "Recall   : 100.0 %\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "print(classification_report(\n",
        "    y_test,\n",
        "    y_pred,\n",
        "    target_names=['Not Returned', 'Returned']\n",
        "))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f73C6xzPmfau",
        "outputId": "4ec5d677-881d-4d1e-d87e-b521db17cb66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "Not Returned       1.00      1.00      1.00       710\n",
            "    Returned       1.00      1.00      1.00       290\n",
            "\n",
            "    accuracy                           1.00      1000\n",
            "   macro avg       1.00      1.00      1.00      1000\n",
            "weighted avg       1.00      1.00      1.00      1000\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix\n",
        "\n",
        "cm = confusion_matrix(y_test, y_pred)\n",
        "\n",
        "print(cm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l8PblzFemiGw",
        "outputId": "fb652622-8575-4f33-b3bc-2b9e620c430c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[710   0]\n",
            " [  0 290]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(6, 5))\n",
        "\n",
        "sns.heatmap(\n",
        "    cm,\n",
        "    annot=True,\n",
        "    fmt='d',\n",
        "    cmap='Blues',\n",
        "    xticklabels=['Not Returned', 'Returned'],\n",
        "    yticklabels=['Not Returned', 'Returned']\n",
        ")\n",
        "\n",
        "plt.title('Confusion Matrix - Logistic Regression')\n",
        "plt.xlabel('Predicted')\n",
        "plt.ylabel('Actual')\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 507
        },
        "id": "AJ2RqqJmmnTg",
        "outputId": "af081ef4-075e-4c33-ead2-7c0f988f938e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x500 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAHqCAYAAAD4YG/CAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAX51JREFUeJzt3Xl8TNf7B/DPZJtEViFrkYRYEmJXRtQaUtRSsZUSa0vtQYlaIlQ0bSltNdSSVOlirWrRWFOE2rcqsaZIYokkguzn98f8Ml8jCTOM3Mzt5/193de3c+659z4zMjx5zjn3KoQQAkREREQyYSJ1AERERESGxOSGiIiIZIXJDREREckKkxsiIiKSFSY3REREJCtMboiIiEhWmNwQERGRrDC5ISIiIllhckNERESywuSG9JKQkIAOHTrA3t4eCoUCmzdvNuj5r127BoVCgejoaIOe15i1bt0arVu3ljqMUrN3714oFArs3bvXIOeLjo6GQqHAtWvXDHI+AsLCwqBQKKQOg6hETG6M0OXLl/H++++jatWqsLS0hJ2dHfz9/bFo0SI8fvz4lV47ODgYZ86cwccff4zVq1ejcePGr/R6pWnQoEFQKBSws7Mr9nNMSEiAQqGAQqHAZ599pvf5b926hbCwMJw8edIA0ZYOT09PvPXWW1KHoZN58+YZPNl+WmGiVLiZmZnhtddew6BBg3Dz5s1Xem0i0p2Z1AGQfn777Tf06tULSqUSAwcORJ06dZCTk4P9+/dj8uTJOHfuHJYtW/ZKrv348WPEx8fjo48+wujRo1/JNTw8PPD48WOYm5u/kvM/j5mZGR49eoRff/0VvXv31tq3Zs0aWFpaIisr64XOfevWLcyePRuenp6oX7++zsf98ccfL3Q9Y9WyZUs8fvwYFhYWeh03b9489OzZE927d9dqHzBgAPr27QulUmmwGMPDw+Hl5YWsrCwcOnQI0dHR2L9/P86ePQtLS0uDXaesmj59OqZOnSp1GEQlYnJjRK5evYq+ffvCw8MDu3fvhpubm2bfqFGjcOnSJfz222+v7Pp37twBADg4OLyyaygUCkn/cVAqlfD398cPP/xQJLlZu3YtOnfujA0bNpRKLI8ePUK5cuX0/kfe2JmYmBj0Z8DU1BSmpqYGOx8AdOzYUVO1HDZsGCpWrIhPPvkEW7ZsKfJz8yoJIZCVlQUrK6tSuyag/iXAzIz/fFDZxWEpIxIZGYnMzEysWLFCK7Ep5O3tjXHjxmle5+XlYc6cOahWrRqUSiU8PT0xbdo0ZGdnax1XOPSwf/9+vP7667C0tETVqlXx3XffafqEhYXBw8MDADB58mQoFAp4enoCUA/nFP73k4obl4+NjUWLFi3g4OAAGxsb1KxZE9OmTdPsL2nOze7du/HGG2/A2toaDg4O6NatG86fP1/s9S5duoRBgwbBwcEB9vb2GDx4MB49elTyB/uUfv36Ydu2bUhLS9O0HTlyBAkJCejXr1+R/qmpqZg0aRL8/PxgY2MDOzs7dOzYEadOndL02bt3L5o0aQIAGDx4sGZYo/B9tm7dGnXq1MGxY8fQsmVLlCtXTvO5PD3nJjg4GJaWlkXef2BgIMqXL49bt27p/F4NQdefs4KCAoSFhcHd3R3lypVDmzZt8Pfff8PT0xODBg3S9Ctuzk1CQgKCgoLg6uoKS0tLVKpUCX379kV6ejoAdVL88OFDxMTEaD7bwnOWNOdm27ZtaNWqFWxtbWFnZ4cmTZpg7dq1L/QZvPHGGwDUQ8ZP+ueff9CzZ084OjrC0tISjRs3xpYtW4ocf/r0abRq1QpWVlaoVKkS5s6di1WrVhWJu/C7umPHDjRu3BhWVlZYunQpACAtLQ3jx49H5cqVoVQq4e3tjU8++QQFBQVa1/rxxx/RqFEjzfv28/PDokWLNPtzc3Mxe/ZsVK9eHZaWlqhQoQJatGiB2NhYTZ/ivtuG/PuG6GUx9TYiv/76K6pWrYrmzZvr1H/YsGGIiYlBz549MXHiRBw+fBgRERE4f/48Nm3apNX30qVL6NmzJ4YOHYrg4GCsXLkSgwYNQqNGjVC7dm306NEDDg4OmDBhAt555x106tQJNjY2esV/7tw5vPXWW6hbty7Cw8OhVCpx6dIlHDhw4JnH7dy5Ex07dkTVqlURFhaGx48f48svv4S/vz+OHz9eJLHq3bs3vLy8EBERgePHj2P58uVwdnbGJ598olOcPXr0wIgRI7Bx40YMGTIEgLpqU6tWLTRs2LBI/ytXrmDz5s3o1asXvLy8kJKSgqVLl6JVq1b4+++/4e7uDh8fH4SHh2PmzJl47733NP8YPvlnee/ePXTs2BF9+/bFu+++CxcXl2LjW7RoEXbv3o3g4GDEx8fD1NQUS5cuxR9//IHVq1fD3d1dp/dpKLr+nIWGhiIyMhJdunRBYGAgTp06hcDAwOcO8+Xk5CAwMBDZ2dkYM2YMXF1dcfPmTWzduhVpaWmwt7fH6tWrMWzYMLz++ut47733AADVqlUr8ZzR0dEYMmQIateujdDQUDg4OODEiRPYvn17sQns8xQmIOXLl9e0nTt3Dv7+/njttdcwdepUWFtb4+eff0b37t2xYcMGvP322wCAmzdvok2bNlAoFAgNDYW1tTWWL19e4jDahQsX8M477+D999/H8OHDUbNmTTx69AitWrXCzZs38f7776NKlSo4ePAgQkNDkZSUhC+++AKA+peLd955B+3atdN8H86fP48DBw5ofjEKCwtDRESE5vPMyMjA0aNHcfz4cbRv377Ez8CQf98QvTRBRiE9PV0AEN26ddOp/8mTJwUAMWzYMK32SZMmCQBi9+7dmjYPDw8BQMTFxWnabt++LZRKpZg4caKm7erVqwKA+PTTT7XOGRwcLDw8PIrEMGvWLPHkj9jChQsFAHHnzp0S4y68xqpVqzRt9evXF87OzuLevXuatlOnTgkTExMxcODAItcbMmSI1jnffvttUaFChRKv+eT7sLa2FkII0bNnT9GuXTshhBD5+fnC1dVVzJ49u9jPICsrS+Tn5xd5H0qlUoSHh2vajhw5UuS9FWrVqpUAIKKioord16pVK622HTt2CABi7ty54sqVK8LGxkZ07979ue9RXx4eHqJz584l7tf15yw5OVmYmZkViTEsLEwAEMHBwZq2PXv2CABiz549QgghTpw4IQCIdevWPTNWa2trrfMUWrVqlQAgrl69KoQQIi0tTdja2oqmTZuKx48fa/UtKCh45jUKz7Vz505x584d8e+//4r169cLJycnoVQqxb///qvp265dO+Hn5yeysrK0zt+8eXNRvXp1TduYMWOEQqEQJ06c0LTdu3dPODo6asUtxP++q9u3b9eKa86cOcLa2lpcvHhRq33q1KnC1NRUJCYmCiGEGDdunLCzsxN5eXklvsd69eo9889ciKLf7Vfx9w3Ry+CwlJHIyMgAANja2urU//fffwcAhISEaLVPnDgRAIrMzfH19dVUEwDAyckJNWvWxJUrV1445qcVztX55ZdfipTKS5KUlISTJ09i0KBBcHR01LTXrVsX7du317zPJ40YMULr9RtvvIF79+5pPkNd9OvXD3v37kVycjJ2796N5OTkEn+jVyqVMDFRf5Xy8/Nx7949zZDb8ePHdb6mUqnE4MGDderboUMHvP/++wgPD0ePHj1gaWmpGZ4oTbr+nO3atQt5eXn44IMPtPqNGTPmudewt7cHAOzYsUOv4cWSxMbG4sGDB5g6dWqRuT26Lm8OCAiAk5MTKleujJ49e8La2hpbtmxBpUqVAKiHKnfv3o3evXvjwYMHuHv3Lu7evYt79+4hMDAQCQkJmtVV27dvh0ql0ppk7ujoiP79+xd7bS8vLwQGBmq1rVu3Dm+88QbKly+vudbdu3cREBCA/Px8xMXFAVB/Bx8+fKg1xPQ0BwcHnDt3DgkJCTp9FkDZ/PuG/tuY3BgJOzs7AMCDBw906n/9+nWYmJjA29tbq93V1RUODg64fv26VnuVKlWKnKN8+fK4f//+C0ZcVJ8+feDv749hw4bBxcUFffv2xc8///zMRKcwzpo1axbZ5+Pjg7t37+Lhw4da7U+/l8KhAn3eS6dOnWBra4uffvoJa9asQZMmTYp8loUKCgqwcOFCVK9eHUqlEhUrVoSTkxNOnz6tmROii9dee02vycOfffYZHB0dcfLkSSxevBjOzs7PPebOnTtITk7WbJmZmTpfrzi6/pwV/v/T/RwdHbWGcorj5eWFkJAQLF++HBUrVkRgYCC+/vprvT7bJxXOi6lTp84LHQ8AX3/9NWJjY7F+/Xp06tQJd+/e1RpGunTpEoQQmDFjBpycnLS2WbNmAQBu374NQP3ZFPezVdLPm5eXV5G2hIQEbN++vci1AgICtK71wQcfoEaNGujYsSMqVaqEIUOGYPv27VrnCg8PR1paGmrUqAE/Pz9MnjwZp0+ffubnURb/vqH/NiY3RsLOzg7u7u44e/asXsfp+ptoSatJhBAvfI38/Hyt11ZWVoiLi8POnTsxYMAAnD59Gn369EH79u2L9H0ZL/NeCimVSvTo0QMxMTHYtGnTM+dhzJs3DyEhIWjZsiW+//577NixA7Gxsahdu7bOFSoAeq94OXHihOYfrTNnzuh0TJMmTeDm5qbZXuR+PcV51Td0+/zzz3H69GlMmzYNjx8/xtixY1G7dm3cuHHjlV63JK+//joCAgIQFBSELVu2oE6dOujXr58mWSz8c580aRJiY2OL3UpKXp6nuJ+TgoICtG/fvsRrBQUFAQCcnZ1x8uRJbNmyBV27dsWePXvQsWNHBAcHa87VsmVLXL58GStXrkSdOnWwfPlyNGzYEMuXL39ubKXx9w2RLjih2Ii89dZbWLZsGeLj46FSqZ7Z18PDAwUFBUhISICPj4+mPSUlBWlpaZqVT4ZQvnx5rZVFhZ7+bQ1QL/Nt164d2rVrhwULFmDevHn46KOPsGfPHs1vmU+/D0A9ifJp//zzDypWrAhra+uXfxPF6NevH1auXAkTExP07du3xH7r169HmzZtsGLFCq32tLQ0VKxYUfPakAnAw4cPMXjwYPj6+qJ58+aIjIzE22+/rVmRVZI1a9Zo3aCwatWqLxWHrj9nhf9/6dIlrcrDvXv3dP5t3c/PD35+fpg+fToOHjwIf39/REVFYe7cuQB0/3wLJxqfPXv2hROMJ5mamiIiIgJt2rTBV199halTp2o+V3Nz82J/rp/k4eGBS5cuFWkvrq0k1apVQ2Zm5nOvBQAWFhbo0qULunTpgoKCAnzwwQdYunQpZsyYofk8HB0dMXjwYAwePBiZmZlo2bIlwsLCMGzYsBLfQ2n9fUOkC1ZujMiHH34Ia2trDBs2DCkpKUX2X758WbOks1OnTgCgWSVRaMGCBQCAzp07GyyuatWqIT09Xat0nZSUVGSFRGpqapFjC+cZPL1ctJCbmxvq16+PmJgYrQTq7Nmz+OOPPzTv81Vo06YN5syZg6+++gqurq4l9jM1NS3yG+e6deuK3LG2MAkrLhHU15QpU5CYmIiYmBgsWLAAnp6eCA4OLvFzLOTv74+AgADN9rLJja4/Z+3atYOZmRm++eYbrX5fffXVc6+RkZGBvLw8rTY/Pz+YmJhovV9ra2udPtsOHTrA1tYWERERRVZqvWjloHXr1nj99dfxxRdfICsrC87OzmjdujWWLl2KpKSkIv0L7xkFqJfwx8fHa925OjU1FWvWrNH5+r1790Z8fDx27NhRZF9aWprm87t3757WPhMTE9StWxfA/76DT/exsbGBt7f3M3+2SvPvGyJdsHJjRKpVq4a1a9eiT58+8PHx0bpD8cGDB7Fu3TrNvT3q1auH4OBgLFu2DGlpaWjVqhX++usvxMTEoHv37mjTpo3B4urbty+mTJmCt99+G2PHjsWjR4/wzTffoEaNGloTasPDwxEXF4fOnTvDw8MDt2/fxpIlS1CpUiW0aNGixPN/+umn6NixI1QqFYYOHapZCm5vb4+wsDCDvY+nmZiYYPr06c/t99ZbbyE8PByDBw9G8+bNcebMGaxZs6ZI4lCtWjU4ODggKioKtra2sLa2RtOmTYudQ/Esu3fvxpIlSzBr1izN0vRVq1ahdevWmDFjBiIjI/U63/NcunRJUx15UoMGDdC5c2edfs5cXFwwbtw4fP755+jatSvefPNNnDp1Ctu2bUPFihWfWXXZvXs3Ro8ejV69eqFGjRrIy8vD6tWrYWpqqhluAYBGjRph586dWLBgAdzd3eHl5YWmTZsWOZ+dnR0WLlyIYcOGoUmTJujXrx/Kly+PU6dO4dGjR4iJiXmhz2ny5Mno1asXoqOjMWLECHz99ddo0aIF/Pz8MHz4cFStWhUpKSmIj4/HjRs3NPdB+vDDD/H999+jffv2GDNmjGYpeJUqVZCamqpTRWry5MnYsmUL3nrrLc2S6ocPH+LMmTNYv349rl27hooVK2LYsGFITU1F27ZtUalSJVy/fh1ffvkl6tevr6m4+Pr6onXr1mjUqBEcHR1x9OhRrF+//pl3JS/Nv2+IdCLlUi16MRcvXhTDhw8Xnp6ewsLCQtja2gp/f3/x5Zdfai07zc3NFbNnzxZeXl7C3NxcVK5cWYSGhmr1EaLk5b5PL0EuaSm4EEL88ccfok6dOsLCwkLUrFlTfP/990WWi+7atUt069ZNuLu7CwsLC+Hu7i7eeecdreWrxS0FF0KInTt3Cn9/f2FlZSXs7OxEly5dxN9//63Vp/B6Ty81f3opcEmeXApekpKWgk+cOFG4ubkJKysr4e/vL+Lj44tdwv3LL78IX19fYWZmpvU+W7VqJWrXrl3sNZ88T0ZGhvDw8BANGzYUubm5Wv0mTJggTExMRHx8/DPfgz4Kl+0Wtw0dOlQIofvPWV5enpgxY4ZwdXUVVlZWom3btuL8+fOiQoUKYsSIEZp+Ty8Fv3LlihgyZIioVq2asLS0FI6OjqJNmzZi586dWuf/559/RMuWLYWVlZXW8vKS/vy3bNkimjdvrvmZev3118UPP/zwzM+j8FxHjhwpsi8/P19Uq1ZNVKtWTbPU+vLly2LgwIHC1dVVmJubi9dee0289dZbYv369VrHnjhxQrzxxhtCqVSKSpUqiYiICLF48WIBQCQnJ2v9eZS0TPvBgwciNDRUeHt7CwsLC1GxYkXRvHlz8dlnn4mcnBwhhBDr168XHTp0EM7OzsLCwkJUqVJFvP/++yIpKUlznrlz54rXX39dODg4CCsrK1GrVi3x8ccfa84hRNGl4EIY/u8bopehEIIzuIhIGmlpaShfvjzmzp2Ljz76SOpwypTx48dj6dKlyMzMNPjjI4jkjnNuiKhUFPek9cI5Gk8+XuK/6OnP5t69e1i9ejVatGjBxIboBXDODRGVip9++gnR0dGaR3fs378fP/zwAzp06AB/f3+pw5OUSqVC69at4ePjg5SUFKxYsQIZGRmYMWOG1KERGSUmN0RUKurWrQszMzNERkYiIyNDM8m4uMnK/zWdOnXC+vXrsWzZMigUCjRs2BArVqxAy5YtpQ6NyChxzg0RERHJCufcEBERkawwuSEiIiJZYXJDREREsiLLCcVWDUq+kyYR6e7+kec/HoGIns+ylP61NfS/f49PGOffAazcEBERkawwuSEiIpILhYlhNz14enpCoVAU2UaNGgUAyMrKwqhRo1ChQgXY2NggKCioyEOgExMT0blzZ5QrVw7Ozs6YPHlykQfn6kKWw1JERET/STo8aPVVOXLkCPLz8zWvz549i/bt26NXr14AgAkTJuC3337DunXrYG9vj9GjR6NHjx44cOAAACA/Px+dO3eGq6srDh48iKSkJAwcOBDm5uaYN2+eXrHI8j43nHNDZBicc0NkGKU256bROIOe7/GxRS987Pjx47F161YkJCQgIyMDTk5OWLt2LXr27AkA+Oeff+Dj44P4+Hg0a9YM27Ztw1tvvYVbt27BxcUFABAVFYUpU6bgzp07sLCw0PnaHJYiIiKSCwMPS2VnZyMjI0Nry87Ofm4YOTk5+P777zFkyBAoFAocO3YMubm5CAgI0PSpVasWqlSpgvj4eABAfHw8/Pz8NIkNAAQGBiIjIwPnzp3T62NgckNERETFioiIgL29vdYWERHx3OM2b96MtLQ0DBo0CACQnJwMCwsLODg4aPVzcXFBcnKyps+TiU3h/sJ9+uCcGyIiIrkw8Jyb0NBQhISEaLUplcrnHrdixQp07NgR7u7uBo1HV0xuiIiI5ELPFU7Po1QqdUpmnnT9+nXs3LkTGzdu1LS5uroiJycHaWlpWtWblJQUuLq6avr89ddfWucqXE1V2EdXHJYiIiIig1m1ahWcnZ3RuXNnTVujRo1gbm6OXbt2adouXLiAxMREqFQqAIBKpcKZM2dw+/ZtTZ/Y2FjY2dnB19dXrxhYuSEiIpILCZeCA0BBQQFWrVqF4OBgmJn9L8Wwt7fH0KFDERISAkdHR9jZ2WHMmDFQqVRo1qwZAKBDhw7w9fXFgAEDEBkZieTkZEyfPh2jRo3Su3rE5IaIiEguDDwspa+dO3ciMTERQ4YMKbJv4cKFMDExQVBQELKzsxEYGIglS5Zo9puammLr1q0YOXIkVCoVrK2tERwcjPDwcL3j4H1uiKhEvM8NkWGU2n1umk0x6PkeH/rEoOcrLazcEBERyYXEw1JlBScUExERkaywckNERCQXEs+5KSuY3BAREckFh6UAcFiKiIiIZIaVGyIiIrngsBQAJjdERETywWEpAByWIiIiIplh5YaIiEguOCwFgMkNERGRfDC5AcBhKSIiIpIZVm6IiIjkwoQTigFWboiIiEhmWLkhIiKSC865AcDkhoiISD54nxsAHJYiIiIimWHlhoiISC44LAWAyQ0REZF8cFgKAIeliIiISGZYuSEiIpILDksBYOWGiIiIZIaVGyIiIrngnBsATG6IiIjkg8NSADgsRURERDLDyg0REZFccFgKAJMbIiIi+eCwFAAOSxEREZHMsHJDREQkFxyWAsDkhoiISD44LAWAw1JEREQkM6zcEBERyQUrNwBYuSEiIiKZYeWGiIhILjihGACTGyIiIvngsBQADksRERGRzLByQ0REJBcclgLA5IaIiEg+OCwFgMNSREREJDOs3BAREckFh6UAMLkhIiKSDQWTGwAcliIiIiKZYeWGiIhIJli5UWPlhoiIiGSFlRsiIiK5YOEGgETJTYMGDXQunR0/fvwVR0NERCQPHJZSk2RYqnv37ujWrRu6deuGwMBAXL58GUqlEq1bt0br1q1haWmJy5cvIzAwUIrwiIiI6AXcvHkT7777LipUqAArKyv4+fnh6NGjmv1CCMycORNubm6wsrJCQEAAEhIStM6RmpqK/v37w87ODg4ODhg6dCgyMzP1ikOSys2sWbM0/z1s2DCMHTsWc+bMKdLn33//Le3QiIiIjJaUlZv79+/D398fbdq0wbZt2+Dk5ISEhASUL19e0ycyMhKLFy9GTEwMvLy8MGPGDAQGBuLvv/+GpaUlAKB///5ISkpCbGwscnNzMXjwYLz33ntYu3atzrEohBDC4O9QD/b29jh69CiqV6+u1Z6QkIDGjRsjPT1d73NaNRhtqPCI/tPuH/lK6hCIZMGylEoJdn2/M+j5Mn4cqHPfqVOn4sCBA/jzzz+L3S+EgLu7OyZOnIhJkyYBANLT0+Hi4oLo6Gj07dsX58+fh6+vL44cOYLGjRsDALZv345OnTrhxo0bcHd31ykWyVdLWVlZ4cCBA0XaDxw4oMniiIiIqGzbsmULGjdujF69esHZ2RkNGjTAt99+q9l/9epVJCcnIyAgQNNmb2+Ppk2bIj4+HgAQHx8PBwcHTWIDAAEBATAxMcHhw4d1jkXy1VLjx4/HyJEjcfz4cbz++usAgMOHD2PlypWYMWOGxNEREREZD0MPS2VnZyM7O1urTalUQqlUFul75coVfPPNNwgJCcG0adNw5MgRjB07FhYWFggODkZycjIAwMXFRes4FxcXzb7k5GQ4Oztr7TczM4Ojo6Omjy4kT26mTp2KqlWrYtGiRfj+++8BAD4+Pli1ahV69+4tcXRERET/XREREZg9e7ZW26xZsxAWFlakb0FBARo3box58+YBUK+MPnv2LKKiohAcHFwa4WpIntwAQO/evZnIEBERvSwDzycODQ1FSEiIVltxVRsAcHNzg6+vr1abj48PNmzYAABwdXUFAKSkpMDNzU3TJyUlBfXr19f0uX37ttY58vLykJqaqjleF5LPuQGAtLQ0LF++HNOmTUNqaioA9f1tbt68KXFkRERExkOhUBh0UyqVsLOz09pKSm78/f1x4cIFrbaLFy/Cw8MDAODl5QVXV1fs2rVLsz8jIwOHDx+GSqUCAKhUKqSlpeHYsWOaPrt370ZBQQGaNm2q8+cgeeXm9OnTCAgIgL29Pa5du4Zhw4bB0dERGzduRGJiIr77zrAzv4mIiMjwJkyYgObNm2PevHno3bs3/vrrLyxbtgzLli0DoE68xo8fj7lz56J69eqapeDu7u7o3r07AHWl580338Tw4cMRFRWF3NxcjB49Gn379tV5pRRQBio3ISEhGDRoEBISErRWR3Xq1AlxcXESRkZERGRcDF250UeTJk2wadMm/PDDD6hTpw7mzJmDL774Av3799f0+fDDDzFmzBi89957aNKkCTIzM7F9+3atf//XrFmDWrVqoV27dujUqRNatGihSZB0/hzKwn1ujh8/jmrVqsHW1hanTp1C1apVcf36ddSsWRNZWVl6n5P3uSEyDN7nhsgwSus+N44DdL/RnS5SV/cz6PlKi+SVG6VSiYyMjCLtFy9ehJOTkwQRERERkTGTPLnp2rUrwsPDkZubC0BdUktMTMSUKVMQFBQkcXRERETGQ8phqbJE8uTm888/R2ZmJpydnfH48WO0atUK3t7esLW1xccffyx1eERERMZDYeDNSEm+Wsre3h6xsbHYv38/Tp8+jczMTDRs2FDr9sxEREREupI8uSnUokULtGjRQuowiIiIjJYxDyUZUplIbnbt2oVdu3bh9u3bKCgo0Nq3cuVKiaIiIiIiYyR5cjN79myEh4ejcePGcHNzY9ZJRET0gvhvqJrkyU1UVBSio6MxYMAAqUMhIiIyakxu1CRfLZWTk4PmzZtLHQYRERHJhOTJzbBhw7B2rWHvqEhERPSfxKXgAMrAsFRWVhaWLVuGnTt3om7dujA3N9fav2DBAokiIyIiMi4cllKTPLk5ffo06tevDwA4e/as1j7+IREREZG+JE1u8vPzMXv2bPj5+aF8+fJShkJERGT0WBRQk3TOjampKTp06IC0tDQpwyAiIpIFPltKTfIJxXXq1MGVK1ekDoOIiIhkQvLkZu7cuZg0aRK2bt2KpKQkZGRkaG1ERESkG1Zu1CSfUNypUycAQNeuXbU+SCEEFAoF8vPzpQqNiIiIjJDkyc2ePXukDoGIiEgejLfYYlCSJzetWrWSOgQiIiJZMOahJEOSPLmJi4t75v6WLVuWUiREREQkB5InN61bty7S9mTmyTk3REREumHlRk3y1VL379/X2m7fvo3t27ejSZMm+OOPP6QOj4iIyGhwtZSa5JUbe3v7Im3t27eHhYUFQkJCcOzYMQmiIiIiImMleXJTEhcXF1y4cEHqMIiIiIyH8RZbDEry5Ob06dNar4UQSEpKwvz58zUP1CQiIiLSleTJTf369aFQKCCE0Gpv1qwZVq5cKVFURERExseY58kYkuTJzdWrV7Vem5iYwMnJCZaWlhJFRC/qn99mw8O9QpH2qJ/iMGH+zxjSwx99OjZG/VqVYGdjBdc3JiM987FW3/J25bBgSi90alkHBUJg866TmBS5Hg8f55TW2yAyGj+uXYOYVStw9+4d1KhZC1OnzYBf3bpSh0USYnKjJvlqqX379sHV1RUeHh7w8PBA5cqVYWlpiZycHHz33XdSh0d6aPHup/AMCNVsnUZ8CQDYGHsCAFDO0hyxB//GpytLXgW3al4wfKq54a2RXyFobBRaNPTG1zP6lUr8RMZk+7bf8VlkBN7/YBR+XLcJNWvWwsj3h+LevXtSh0YkOcmTm8GDByM9Pb1I+4MHDzB48GAJIqIXdfd+JlLuPdBsnd6og8uJd/DnsQQAwFdr9+KzVbE4fPpascfX9HJBoH9tfBC+FkfOXsfBk1cQ8sk69ApsCDenoqvqiP7LVsesQo+evdH97SBU8/bG9FmzYWlpic0bN0gdGkmIS8HVJE9uCh+Q+bQbN24Uu0ycjIO5mSn6dmqCmF/idT6maV0v3M94hON/J2radh++gIICgSZ1PF5FmERGKTcnB+f/PodmquaaNhMTEzRr1hynT52QMDKSGpMbNcnm3DRo0EDz4bVr1w5mZv8LJT8/H1evXsWbb74pVXj0krq2qQsHWyt8/+thnY9xqWCHO6kPtNry8wuQmvEILhXtDB0ikdG6n3Yf+fn5qFBBe45bhQoVcPXqFYmiIio7JEtuunfvDgA4efIkAgMDYWNjo9lnYWEBT09PBAUFPfc82dnZyM7O1moTBflQmJgaNF7ST3D35thx4G8k3Sk65EhERK+I8RZbDEqy5GbWrFkAAE9PT/Tp0+eFV0dFRERg9uzZWm2mLk1g7vb6S8dIL6aKW3m0bVoTfSd9q9dxKfcy4ORoq9VmamoCR7tySLmbYcgQiYxaeYfyMDU1LTJ5+N69e6hYsaJEUVFZYMxDSYYk+Zyb4OBgZGVlYfny5QgNDUVqaioA4Pjx47h58+Zzjw8NDUV6errWZubS6FWHTc8woKsKt1MfYNuf5/Q67vDpqyhvVw4NfCpr2lo3qQETEwWOnL1u6DCJjJa5hQV8fGvj8KH/zWkrKCjA4cPxqFuvgYSREZUNkt/n5vTp0wgICIC9vT2uXbuG4cOHw9HRERs3bkRiYuJzl4MrlUoolUqtNg5JSUehUGBgt2ZYs/Uw8vMLtPa5VLCFSwU7VKui/s2yTnV3PHiYhX+T7+N+xiNcuJqCHQfO4esZ/TD24x9hbmaKhVN7Y92O4xzeInrKgODBmDFtCmrXroM6fnXx/eoYPH78GN3f7iF1aCQhVm7UJE9uJkyYgEGDBiEyMhK2tv8bkujUqRP69eP9TYxN26Y1UcXNETGbDxXZN6znG5g+opPm9c6VEwAAw2eu1kw8HjwtBgun9sbvS8egoEB9E7+JketKJ3giI/Jmx064n5qKJV8txt27d1Czlg+WLF2OChyWIoJCPP3cg1Jmb2+P48ePo1q1arC1tcWpU6dQtWpVXL9+HTVr1kRWVpbe57RqMPoVREr033P/yFdSh0AkC5alVErwnrTNoOe79FlHg56vtEheuVEqlcjIKDpZ9OLFi3BycpIgIiIiIuPEYSk1yScUd+3aFeHh4cjNzQWg/oNJTEzElClTdFoKTkRERPQkyZObzz//HJmZmXB2dsbjx4/RqlUreHt7w8bGBh9//LHU4RERERkNhcKwm7GSfFjK3t4esbGx2L9/P06fPo3MzEw0bNgQAQEBUodGRERkVDgspSZ5clOoRYsWaNGiheb18ePHMXPmTGzdulXCqIiIiMjYSDostWPHDkyaNAnTpk3DlSvq56H8888/6N69O5o0aYKCgoLnnIGIiIgKcVhKTbLKzYoVKzQ37Lt//z6WL1+OBQsWYMyYMejTpw/Onj0LHx8fqcIjIiIyOiYmRpyRGJBklZtFixbhk08+wd27d/Hzzz/j7t27WLJkCc6cOYOoqCgmNkRERPRCJKvcXL58Gb169QIA9OjRA2ZmZvj0009RqVIlqUIiIiIyasY8lGRIklVuHj9+jHLlygFQz+5WKpVwc3OTKhwiIiJ6CWFhYVAoFFpbrVq1NPuzsrIwatQoVKhQATY2NggKCkJKSorWORITE9G5c2eUK1cOzs7OmDx5MvLy8vSORdLVUsuXL4eNjQ0AIC8vD9HR0aj41HNRxo4dK0VoRERERkfqpeC1a9fGzp07Na/NzP6XZkyYMAG//fYb1q1bB3t7e4wePRo9evTAgQMHAAD5+fno3LkzXF1dcfDgQSQlJWHgwIEwNzfHvHnz9IpDsmdLeXp6PvcPQaFQaFZR6YPPliIyDD5bisgwSuvZUn4zYg16vjNz2uvcNywsDJs3b8bJkyeL7EtPT4eTkxPWrl2Lnj17AlCvjvbx8UF8fDyaNWuGbdu24a233sKtW7fg4uICAIiKisKUKVNw584dWFhY6ByLZJWba9euSXVpIiIiegUSEhLg7u4OS0tLqFQqREREoEqVKjh27Bhyc3O1btBbq1YtVKlSRZPcxMfHw8/PT5PYAEBgYCBGjhyJc+fOoUGDBjrHUWZu4kdEREQvx9DDUtnZ2cjOztZqUyqVUCqVRfo2bdoU0dHRqFmzJpKSkjB79my88cYbOHv2LJKTk2FhYQEHBwetY1xcXJCcnAwASE5O1kpsCvcX7tOH5M+WIiIiIsN4ekLvy24RERGwt7fX2iIiIoq9dseOHdGrVy/UrVsXgYGB+P3335GWloaff/65lD8FJjdERERUgtDQUKSnp2ttoaGhOh3r4OCAGjVq4NKlS3B1dUVOTg7S0tK0+qSkpMDV1RUA4OrqWmT1VOHrwj66YnJDREQkE4Z+/IJSqYSdnZ3WVtyQVHEyMzNx+fJluLm5oVGjRjA3N8euXbs0+y9cuIDExESoVCoAgEqlwpkzZ3D79m1Nn9jYWNjZ2cHX11evz4FzboiIiOilTZo0CV26dIGHhwdu3bqFWbNmwdTUFO+88w7s7e0xdOhQhISEwNHREXZ2dhgzZgxUKhWaNWsGAOjQoQN8fX0xYMAAREZGIjk5GdOnT8eoUaN0TqgKSZ7cmJqaIikpCc7Ozlrt9+7dg7OzM/Lz8yWKjIiIyLhIeZ+bGzdu4J133sG9e/fg5OSEFi1a4NChQ3BycgIALFy4ECYmJggKCkJ2djYCAwOxZMkSzfGmpqbYunUrRo4cCZVKBWtrawQHByM8PFzvWCS7z00hExMTJCcnF0lubt26hWrVquHx48d6n5P3uSEyDN7nhsgwSus+Nw3Ddxv0fMdntjXo+UqLZJWbxYsXA1BnmU/eqRhQ36UwLi5O67bNRERERLqQLLlZuHAhAEAIgaioKJiammr2WVhYwNPTE1FRUVKFR0REZHSkfvxCWSFZcnP16lUAQJs2bbBx40aUL19eqlCIiIhkgbmNmuQTivfs2aP578LpP8w8iYiI6EWVifvcfPfdd/Dz84OVlRWsrKxQt25drF69WuqwiIiIjIqh71BsrCSv3CxYsAAzZszA6NGj4e/vDwDYv38/RowYgbt372LChAkSR0hERGQcjDgfMSjJk5svv/wS33zzDQYOHKhp69q1K2rXro2wsDAmN0RERKQXyZObpKQkNG/evEh78+bNkZSUJEFERERExsmYh5IMSfI5N97e3sU+MfSnn35C9erVJYiIiIiIjJnklZvZs2ejT58+iIuL08y5OXDgAHbt2iXJY9KJiIiMFQs3apInN0FBQTh8+DAWLlyIzZs3AwB8fHzw119/oUGDBtIGR0REZEQ4LKUmeXIDAI0aNcL3338vdRhEREQkA2UiuSEiIqKXx8KNmmTJjYmJyXPLZwqFAnl5eaUUERERkXHjsJSaZMnNpk2bStwXHx+PxYsXo6CgoBQjIiIiIjmQLLnp1q1bkbYLFy5g6tSp+PXXX9G/f3+Eh4dLEBkREZFxYuFGTfL73ADArVu3MHz4cPj5+SEvLw8nT55ETEwMPDw8pA6NiIiIjIykyU16ejqmTJkCb29vnDt3Drt27cKvv/6KOnXqSBkWERGRUeKDM9UkG5aKjIzEJ598AldXV/zwww/FDlMRERGR7ow5ITEkyZKbqVOnwsrKCt7e3oiJiUFMTEyx/TZu3FjKkREREZExkyy5GThwIDNMIiIiA+I/q2qSJTfR0dFSXZqIiEiWWDRQKxOrpYiIiIgMhY9fICIikgkWbtSY3BAREckEh6XUOCxFREREssLKDRERkUywcKPGyg0RERHJCis3REREMmHC0g0AJjdERESywdxGjcNSREREJCus3BAREckEl4KrMbkhIiKSCRPmNgA4LEVEREQyw8oNERGRTHBYSo3JDRERkUwwt1HjsBQRERHJCis3REREMqEASzcAKzdEREQkM6zcEBERyQSXgqsxuSEiIpIJrpZS47AUERERyQorN0RERDLBwo0akxsiIiKZMGF2A4DDUkRERCQzrNwQERHJBAs3aqzcEBERkcHNnz8fCoUC48eP17RlZWVh1KhRqFChAmxsbBAUFISUlBSt4xITE9G5c2eUK1cOzs7OmDx5MvLy8vS6NpMbIiIimVAoFAbdXtSRI0ewdOlS1K1bV6t9woQJ+PXXX7Fu3Trs27cPt27dQo8ePTT78/Pz0blzZ+Tk5ODgwYOIiYlBdHQ0Zs6cqdf1mdwQERHJhEJh2O1FZGZmon///vj2229Rvnx5TXt6ejpWrFiBBQsWoG3btmjUqBFWrVqFgwcP4tChQwCAP/74A3///Te+//571K9fHx07dsScOXPw9ddfIycnR+cYmNwQERGRwYwaNQqdO3dGQECAVvuxY8eQm5ur1V6rVi1UqVIF8fHxAID4+Hj4+fnBxcVF0ycwMBAZGRk4d+6czjFwQjEREZFMGHopeHZ2NrKzs7XalEollEplsf1//PFHHD9+HEeOHCmyLzk5GRYWFnBwcNBqd3FxQXJysqbPk4lN4f7Cfbpi5YaIiEgmFAbeIiIiYG9vr7VFREQUe+1///0X48aNw5o1a2BpafkK3+XzMbkhIiKiYoWGhiI9PV1rCw0NLbbvsWPHcPv2bTRs2BBmZmYwMzPDvn37sHjxYpiZmcHFxQU5OTlIS0vTOi4lJQWurq4AAFdX1yKrpwpfF/bRBZMbIiIimTD0aimlUgk7OzutraQhqXbt2uHMmTM4efKkZmvcuDH69++v+W9zc3Ps2rVLc8yFCxeQmJgIlUoFAFCpVDhz5gxu376t6RMbGws7Ozv4+vrq/Dlwzg0REZFMmEh4Ez9bW1vUqVNHq83a2hoVKlTQtA8dOhQhISFwdHSEnZ0dxowZA5VKhWbNmgEAOnToAF9fXwwYMACRkZFITk7G9OnTMWrUqBKTquIwuSEiIqJSsXDhQpiYmCAoKAjZ2dkIDAzEkiVLNPtNTU2xdetWjBw5EiqVCtbW1ggODkZ4eLhe11EIIYShg5eaVYPRUodAJAv3j3wldQhEsmBZSqWEd78/ZdDzff9uPYOer7To9HFv2bJF5xN27dr1hYMhIiIielk6JTfdu3fX6WQKhQL5+fkvEw8RERG9ID44U02n5KagoOBVx0FEREQv6WWeByUnXApOREREsvJCU5wePnyIffv2ITExsciDrMaOHWuQwIiIiEg/Ui4FL0v0Tm5OnDiBTp064dGjR3j48CEcHR1x9+5dlCtXDs7OzkxuiIiIJMJhKTW9h6UmTJiALl264P79+7CyssKhQ4dw/fp1NGrUCJ999tmriJGIiIhIZ3onNydPnsTEiRNhYmICU1NTZGdno3LlyoiMjMS0adNeRYxERESkA0M/ONNY6Z3cmJubw8REfZizszMSExMBAPb29vj3338NGx0RERHpzEShMOhmrPSec9OgQQMcOXIE1atXR6tWrTBz5kzcvXsXq1evLvJMCSIiIqLSpnflZt68eXBzcwMAfPzxxyhfvjxGjhyJO3fuYNmyZQYPkIiIiHSjUBh2M1Z6V24aN26s+W9nZ2ds377doAERERERvQw+FZyIiEgmuBRcTe/kxsvL65kf3pUrV14qICIiInoxzG3U9E5uxo8fr/U6NzcXJ06cwPbt2zF58mRDxUVERET0QvRObsaNG1ds+9dff42jR4++dEBERET0Yox5+bYhGezBmR07dsSGDRsMdToiIiLSE1dLqRksuVm/fj0cHR0NdToiIiKiF/JCN/F7ckKxEALJycm4c+cOlixZYtDgiIiISHdcLaWmd3LTrVs3rQ/PxMQETk5OaN26NWrVqmXQ4IiIiIj0pRBCCKmDMLSsPKkjIJKHZYeuSh0CkSyMbeFVKtcZs+m8Qc/35ds+Bj1fadF7zo2pqSlu375dpP3evXswNTU1SFBERESkP4VCYdDNWOmd3JRU6MnOzoaFhcVLB0RERET0MnSec7N48WIA6qxw+fLlsLGx0ezLz89HXFwc59wQERFJyMR4iy0GpXNys3DhQgDqyk1UVJTWEJSFhQU8PT0RFRVl+AiJiIhIJ0xu1HRObq5eVU8sbNOmDTZu3Ijy5cu/sqCIiIiIXpTeS8H37NnzKuIgIiKil2TMk4ANSe8JxUFBQfjkk0+KtEdGRqJXr14GCYqIiIj0Z6Iw7Gas9E5u4uLi0KlTpyLtHTt2RFxcnEGCIiIiInpReg9LZWZmFrvk29zcHBkZGQYJioiIiPTHUSk1vSs3fn5++Omnn4q0//jjj/D19TVIUEREREQvSu/KzYwZM9CjRw9cvnwZbdu2BQDs2rULa9euxfr16w0eIBEREenGhKUbAC+Q3HTp0gWbN2/GvHnzsH79elhZWaFevXrYvXs3HB0dX0WMREREpAO9h2NkSu/kBgA6d+6Mzp07AwAyMjLwww8/YNKkSTh27Bjy8/MNGiARERGRPl44yYuLi0NwcDDc3d3x+eefo23btjh06JAhYyMiIiI9KBSG3YyVXpWb5ORkREdHY8WKFcjIyEDv3r2RnZ2NzZs3czIxERGRxDjnRk3nyk2XLl1Qs2ZNnD59Gl988QVu3bqFL7/88lXGRkRERKQ3nSs327Ztw9ixYzFy5EhUr179VcZEREREL4CFGzWdKzf79+/HgwcP0KhRIzRt2hRfffUV7t69+ypjIyIiIj3w8QtqOic3zZo1w7fffoukpCS8//77+PHHH+Hu7o6CggLExsbiwYMHrzJOIiIiIp3ovVrK2toaQ4YMwf79+3HmzBlMnDgR8+fPh7OzM7p27foqYiQiIiIdmCgUBt2M1Uvd76dmzZqIjIzEjRs38MMPPxgqJiIiIqIX9kI38Xuaqakpunfvju7duxvidERERPQCjLjYYlAGSW6IiIhIesY8CdiQ+BgKIiIikhVWboiIiGRCAZZuAFZuiIiIZEPK+9x88803qFu3Luzs7GBnZweVSoVt27Zp9mdlZWHUqFGoUKECbGxsEBQUhJSUFK1zJCYmonPnzihXrhycnZ0xefJk5OXl6f856H0EERER0VMqVaqE+fPn49ixYzh69Cjatm2Lbt264dy5cwCACRMm4Ndff8W6deuwb98+3Lp1Cz169NAcn5+fj86dOyMnJwcHDx5ETEwMoqOjMXPmTL1jUQghhMHeWRmRpX+SR0TFWHboqtQhEMnC2BZepXKdyD2XDXq+D9tUe6njHR0d8emnn6Jnz55wcnLC2rVr0bNnTwDAP//8Ax8fH8THx6NZs2bYtm0b3nrrLdy6dQsuLi4AgKioKEyZMgV37tyBhYWFztdl5YaIiIgMKj8/Hz/++CMePnwIlUqFY8eOITc3FwEBAZo+tWrVQpUqVRAfHw8AiI+Ph5+fnyaxAYDAwEBkZGRoqj+64oRiIiIimVAY+EY32dnZyM7O1mpTKpVQKpXF9j9z5gxUKhWysrJgY2ODTZs2wdfXFydPnoSFhQUcHBy0+ru4uCA5ORkAkJycrJXYFO4v3KcPVm6IiIhkwtATiiMiImBvb6+1RURElHj9mjVr4uTJkzh8+DBGjhyJ4OBg/P3336X4CaixckNERETFCg0NRUhIiFZbSVUbALCwsIC3tzcAoFGjRjhy5AgWLVqEPn36ICcnB2lpaVrVm5SUFLi6ugIAXF1d8ddff2mdr3A1VWEfXbFyQ0REJBMKhWE3pVKpWdpduD0ruXlaQUEBsrOz0ahRI5ibm2PXrl2afRcuXEBiYiJUKhUAQKVS4cyZM7h9+7amT2xsLOzs7ODr66vX58DKDRERkUxI+STv0NBQdOzYEVWqVMGDBw+wdu1a7N27Fzt27IC9vT2GDh2KkJAQODo6ws7ODmPGjIFKpUKzZs0AAB06dICvry8GDBiAyMhIJCcnY/r06Rg1apReCRXA5IaIiIgM4Pbt2xg4cCCSkpJgb2+PunXrYseOHWjfvj0AYOHChTAxMUFQUBCys7MRGBiIJUuWaI43NTXF1q1bMXLkSKhUKlhbWyM4OBjh4eF6x8L73BBRiXifGyLDKK373Czeb9jvbGnFbWis3BAREcmEhKNSZQonFBMREZGssHJDREQkEyZ8KjgAVm6IiIhIZli5ISIikgnOuVFjckNERCQTJkxuAHBYioiIiGSGlRsiIiKZkPIOxWUJkxsiIiKZYG6jxmEpIiIikhVWboiIiGSCw1JqTG6IiIhkgrmNGoeliIiISFZYuSEiIpIJVizU+DkQERGRrLByQ0REJBMKTroBwOSGiIhINpjaqHFYioiIiGSFlRsiIiKZ4H1u1JjcEBERyQRTGzUOSxEREZGssHJDREQkExyVUmPlhoiIiGSFlRsiIiKZ4H1u1JjcEBERyQSHY9T4ORAREZGssHJDREQkExyWUmNyQ0REJBNMbdQ4LEVERESywsoNERGRTHBYSo3JDRERkUxwOEaNnwMRERHJCis3REREMsFhKTVWboiIiEhWWLkhIiKSCdZt1CRLbjIyMnTua2dn9wojISIikgeOSqlJltw4ODjoPDaYn5//iqMhIiIiuZAsudmzZ4/mv69du4apU6di0KBBUKlUAID4+HjExMQgIiJCqhCJiIiMigkHpgBImNy0atVK89/h4eFYsGAB3nnnHU1b165d4efnh2XLliE4OFiKEImIiIwKh6XUysRqqfj4eDRu3LhIe+PGjfHXX39JEBEREREZqzKR3FSuXBnffvttkfbly5ejcuXKEkRERERkfBQG/p+xKhNLwRcuXIigoCBs27YNTZs2BQD89ddfSEhIwIYNGySOjoiIiIxJmajcdOrUCRcvXkSXLl2QmpqK1NRUdOnSBRcvXkSnTp2kDo+IiMgoKBSG3YxVmajcAOqhqXnz5kkdBhERkdHiaim1MlG5AYA///wT7777Lpo3b46bN28CAFavXo39+/dLHBkREREZkzKR3GzYsAGBgYGwsrLC8ePHkZ2dDQBIT09nNYeIiEhHHJZSKxPJzdy5cxEVFYVvv/0W5ubmmnZ/f38cP35cwsiIiIiMh5TJTUREBJo0aQJbW1s4Ozuje/fuuHDhglafrKwsjBo1ChUqVICNjQ2CgoKQkpKi1ScxMRGdO3dGuXLl4OzsjMmTJyMvL0+vWMpEcnPhwgW0bNmySLu9vT3S0tJKPyAiIiLSy759+zBq1CgcOnQIsbGxyM3NRYcOHfDw4UNNnwkTJuDXX3/FunXrsG/fPty6dQs9evTQ7M/Pz0fnzp2Rk5ODgwcPIiYmBtHR0Zg5c6ZesZSJCcWurq64dOkSPD09tdr379+PqlWrShMUERGRkZHy3jTbt2/Xeh0dHQ1nZ2ccO3YMLVu2RHp6OlasWIG1a9eibdu2AIBVq1bBx8cHhw4dQrNmzfDHH3/g77//xs6dO+Hi4oL69etjzpw5mDJlCsLCwmBhYaFTLGWicjN8+HCMGzcOhw8fhkKhwK1bt7BmzRpMmjQJI0eOlDo8IiIio2CiMOz2MtLT0wEAjo6OAIBjx44hNzcXAQEBmj61atVClSpVEB8fD0D9xAI/Pz+4uLho+gQGBiIjIwPnzp3T+dplonIzdepUFBQUoF27dnj06BFatmwJpVKJSZMmYcyYMVKHR0RE9J+UnZ2tWeRTSKlUQqlUPvO4goICjB8/Hv7+/qhTpw4AIDk5GRYWFnBwcNDq6+LiguTkZE2fJxObwv2F+3RVJio3CoUCH330EVJTU3H27FkcOnQId+7cwZw5c6QOjYiIyGgY+vELERERsLe319oiIiKeG8eoUaNw9uxZ/Pjjj6XwrosqE5WbQhYWFvD19ZU6DCIiIgIQGhqKkJAQrbbnVW1Gjx6NrVu3Ii4uDpUqVdK0u7q6IicnB2lpaVrVm5SUFLi6umr6PP3A7MLVVIV9dFEmKjcPHz7EjBkz0Lx5c3h7e6Nq1apaGxERET2foZeCK5VK2NnZaW0lJTdCCIwePRqbNm3C7t274eXlpbW/UaNGMDc3x65duzRtFy5cQGJiIlQqFQBApVLhzJkzuH37tqZPbGws7Ozs9Cp+lInKzbBhw7Bv3z4MGDAAbm5uUBjznYOIiIgkIuVqqVGjRmHt2rX45ZdfYGtrq5kjY29vDysrK9jb22Po0KEICQmBo6Mj7OzsMGbMGKhUKjRr1gwA0KFDB/j6+mLAgAGIjIxEcnIypk+fjlGjRj23YvQkhRBCvJJ3qQcHBwf89ttv8Pf3N8j5svS71w8RlWDZoatSh0AkC2NbeD2/kwHsvZBq0PO1rumoc9+SChOrVq3CoEGDAKhv4jdx4kT88MMPyM7ORmBgIJYsWaI15HT9+nWMHDkSe/fuhbW1NYKDgzF//nyYmelejykTyY2Xlxd+//13+Pj4GOR8TG6IDIPJDZFhlFZyE3fRsMlNyxq6JzdlSZmYczNnzhzMnDkTjx49kjoUIiIio2Xo1VLGqkzMufn8889x+fJluLi4wNPTU+v5UgD4fCmZ+XHtGsSsWoG7d++gRs1amDptBvzq1pU6LKIy4dhvP+LK8QO4n3QDZhYWcK3mC1WvISjvWlnTJ/32LRz4eTmSEs4hPy8XVeo0Qst+H6CcfXlNn6zMB4hbuwTXTqlvjlqtkT9avDMSFpZWUrwtolJVJpKb7t27Sx0ClZLt237HZ5ERmD5rNvz86mHN6hiMfH8oftm6HRUqVJA6PCLJ3bp4BnXadIGzVw2IggIc2rAKWz7/CP3mLoO50hK52VnYsuAjVKzshe6T5wMADm/6Dr99OQs9p30BhYm6IB/77Sd4mJ6KrhPnoSA/D7tXLsDe7xahw3tTpXx79IpxPY6a5MlNXl4eFAoFhgwZorUenuRpdcwq9OjZG93fDgIATJ81G3Fxe7F54wYMHf6exNERSa/LhI+1XrcbOhErx/fFnWsJcK/ph6SEc3hwNwV9Zn0FCyvr/+8zCcvH9sSNf06ism9DpN5KROLZo+g1YzGcPWsAAN7o9wG2LpoB/17DYV2ev0jIFXMbNcnn3JiZmeHTTz/V+3HmZHxyc3Jw/u9zaKZqrmkzMTFBs2bNcfrUCQkjIyq7sv9/LqLS2hYAkJ+XCygAU7P/Dd+bmZtDoVAgKUH97J3ky+ehLGejSWwAoLJvAygUCqRc/acUoyeShuTJDQC0bdsW+/btkzoMesXup91Hfn5+keGnChUq4O7duxJFRVR2iYIC7P8xCm7evqhQyRMA4FqtFsyVlji4fiVys7OQm52FAz8vhygowMN09UqZRxn3YWVrr3UuE1NTWFrb4lH6/dJ+G1SKTBQKg27GSvJhKQDo2LEjpk6dijNnzqBRo0awtrbW2t+1a9cSjy3uoV7C9PkP9SIiKuv2rfkaqTevocfUzzVtVrYOCBzxEfZ9/xVO7/oFCoUC1V9vDScPbygUZeL3VSLJlYnk5oMPPgAALFiwoMg+hUKB/Pz8Eo+NiIjA7Nmztdo+mjEL02eGGTRGennlHcrD1NQU9+7d02q/d+8eKlasKFFURGVT3Jqvcf3UYbw95TPYODpp7atSpxEGzF+Fxw/SYWJqCmU5G6yc8A68X1ffCK2cXXk8fpCudUxBfj6yHj7QWlFF8mO8tRbDKhNpfkFBQYnbsxIbQP1Qr/T0dK1t8pTQUoqc9GFuYQEf39o4fChe01ZQUIDDh+NRt14DCSMjKjuEEIhb8zWuHD+IbpM/gZ1TyQ8LtLK1h7KcDW6cP4nHD9LgVV99C3vXaj7IfpSJ29cSNH1vnD8JIQRcvGq98vdAElIYeDNSZaJy8zKUyqJDULxDcdk1IHgwZkybgtq166COX118vzoGjx8/Rve3e0gdGlGZEPf917h4eA86jZkFc0srzTwapZU1zCzUf9ed3/8HyrtVhpWtPZIvn8efP0ShXvu3NffCcXSvgip1GmNPzBdoPWAsCvLzELd2Caq/3oorpeg/oUwkN+Hh4c/cP3PmzFKKhF61Nzt2wv3UVCz5ajHu3r2DmrV8sGTpclTgsBQRAODs3q0AgM2RH2q1tx0cAp8WHQAAack3EL9hFbIfPoBtRRc07twX9Tpo/4LQfvgUxK39Gr98NhUKEwWqNmyBN/qNLJ03QZIx5rsKG1KZeLZUgwbaQxK5ubm4evUqzMzMUK1aNb3vUMzKDZFh8NlSRIZRWs+W+utK+vM76eH1qvbP71QGlYnKzYkTRe9xkpGRgUGDBuHtt9+WICIiIiIyVmViQnFx7OzsMHv2bMyYMUPqUIiIiIwC5xOrldnkBoBm9RMRERGRrsrEsNTixYu1XgshkJSUhNWrV6Njx44SRUVERGRkjLncYkBlIrlZuHCh1msTExM4OTkhODgYoaG8Zw0REZEuuFpKrUwkN1evckUGERERGUaZmHMzZMgQPHjwoEj7w4cPMWTIEAkiIiIiMj4KhWE3Y1UmkpuYGPVdap/2+PFjfPfddxJEREREZHy4WkpN0mGpjIwMCCEghMCDBw9gaWmp2Zefn4/ff/8dzs7OEkZIRERExkbS5MbBwQEKhQIKhQI1atQosl+hUBR54jcRERGVwJjLLQYkaXKzZ88eCCHQtm1bbNiwAY6Ojpp9FhYW8PDwgLu7u4QREhERGQ+ullKTNLlp1aoVAPVqqSpVqkBhzLOXiIiIqEwoExOKPTw8sH//frz77rto3rw5bt68CQBYvXo19u/fL3F0RERExoGrpdTKRHKzYcMGBAYGwsrKCsePH0d2djYA9eMX5s2bJ3F0REREZEzKRHIzd+5cREVF4dtvv4W5ubmm3d/fH8ePH5cwMiIiIuPBpeBqZeIOxRcuXEDLli2LtNvb2yMtLa30AyIiIjJGxpyRGFCZqNy4urri0qVLRdr379+PqlWrShARERERGasykdwMHz4c48aNw+HDh6FQKHDr1i2sWbMGEydOxMiRI6UOj4iIyCgoDPw/Y1UmhqWmTp2KgoICtGvXDo8ePULLli2hVCoxefJkDBs2TOrwiIiIjIIxr3AypDJRuVEoFPjoo4+QmpqKs2fP4tChQ7hz5w7s7e3h5eUldXhERERkRCRNbrKzsxEaGorGjRvD398fv//+O3x9fXHu3DnUrFkTixYtwoQJE6QMkYiIyGhwtZSapMNSM2fOxNKlSxEQEICDBw+iV69eGDx4MA4dOoTPP/8cvXr1gqmpqZQhEhERGQ9jzkgMSNLkZt26dfjuu+/QtWtXnD17FnXr1kVeXh5OnTrFRzEQERHRC5E0ublx4wYaNWoEAKhTpw6USiUmTJjAxIaIiOgFGPMKJ0OSdM5Nfn4+LCwsNK/NzMxgY2MjYURERERk7CSt3AghMGjQICiVSgBAVlYWRowYAWtra61+GzdulCI8IiIio8KBDzVJk5vg4GCt1++++65EkRARERk/5jZqkiY3q1atkvLyREREJENl4g7FREREZAAs3QBgckNERCQbXC2lViYev0BERERkKKzcEBERyQRXS6mxckNERESywsoNERGRTLBwo8bKDRERkVxI+FjwuLg4dOnSBe7u7lAoFNi8ebPWfiEEZs6cCTc3N1hZWSEgIAAJCQlafVJTU9G/f3/Y2dnBwcEBQ4cORWZmpn6BgMkNERERGcDDhw9Rr149fP3118Xuj4yMxOLFixEVFYXDhw/D2toagYGByMrK0vTp378/zp07h9jYWGzduhVxcXF477339I5FIYQQL/xOyqisPKkjIJKHZYeuSh0CkSyMbeFVKtdJSHls0PNVd7F6oeMUCgU2bdqE7t27A1BXbdzd3TFx4kRMmjQJAJCeng4XFxdER0ejb9++OH/+PHx9fXHkyBE0btwYALB9+3Z06tQJN27cgLu7u87XZ+WGiIhIJhQKw26GcvXqVSQnJyMgIEDTZm9vj6ZNmyI+Ph4AEB8fDwcHB01iAwABAQEwMTHB4cOH9boeJxQTERFRsbKzs5Gdna3VplQqNQ+81lVycjIAwMXFRavdxcVFsy85ORnOzs5a+83MzODo6KjpoytWboiIiGTC0POJIyIiYG9vr7VFRESU7pt6AazcEBERyYWB14KHhoYiJCREq03fqg0AuLq6AgBSUlLg5uamaU9JSUH9+vU1fW7fvq11XF5eHlJTUzXH64qVGyIiIiqWUqmEnZ2d1vYiyY2XlxdcXV2xa9cuTVtGRgYOHz4MlUoFAFCpVEhLS8OxY8c0fXbv3o2CggI0bdpUr+uxckNERCQTUj44MzMzE5cuXdK8vnr1Kk6ePAlHR0dUqVIF48ePx9y5c1G9enV4eXlhxowZcHd316yo8vHxwZtvvonhw4cjKioKubm5GD16NPr27avXSimAyQ0REREZwNGjR9GmTRvN68LhrODgYERHR+PDDz/Ew4cP8d577yEtLQ0tWrTA9u3bYWlpqTlmzZo1GD16NNq1awcTExMEBQVh8eLFesfC+9wQUYl4nxsiwyit+9xcvZv1/E568Kpo+fxOZRArN0RERDLBZ0upcUIxERERyQorN0RERHLB0g0AJjdERESyIeVqqbKEw1JEREQkK6zcEBERyYQhH3ZpzJjcEBERyQRzGzUOSxEREZGssHJDREQkExyWUmPlhoiIiGSFlRsiIiLZYOkGYHJDREQkGxyWUuOwFBEREckKKzdEREQywcKNGpMbIiIimeCwlBqHpYiIiEhWWLkhIiKSCT44U42VGyIiIpIVVm6IiIjkgoUbAExuiIiIZIO5jRqHpYiIiEhWWLkhIiKSCS4FV2NyQ0REJBNcLaXGYSkiIiKSFVZuiIiI5IKFGwBMboiIiGSDuY0ah6WIiIhIVli5ISIikgmullJj5YaIiIhkhZUbIiIimeBScDUmN0RERDLBYSk1DksRERGRrDC5ISIiIlnhsBQREZFMcFhKjZUbIiIikhVWboiIiGSCq6XUWLkhIiIiWWHlhoiISCY450aNyQ0REZFMMLdR47AUERERyQorN0RERHLB0g0AJjdERESywdVSahyWIiIiIllh5YaIiEgmuFpKjckNERGRTDC3UeOwFBEREckKkxsiIiK5UBh4ewFff/01PD09YWlpiaZNm+Kvv/56iTf0YpjcEBERkUH89NNPCAkJwaxZs3D8+HHUq1cPgYGBuH37dqnGweSGiIhIJhQG/p++FixYgOHDh2Pw4MHw9fVFVFQUypUrh5UrV76Cd1syJjdEREQyoVAYdtNHTk4Ojh07hoCAAE2biYkJAgICEB8fb+B3+mxcLUVERETFys7ORnZ2tlabUqmEUqks0vfu3bvIz8+Hi4uLVruLiwv++eefVxrn02SZ3FjK8l3JS3Z2NiIiIhAaGlrsl4TKhrEtvKQOgZ6B3yN6mqH//QubG4HZs2drtc2aNQthYWGGvZCBKYQQQuog6L8nIyMD9vb2SE9Ph52dndThEBklfo/oVdOncpOTk4Ny5cph/fr16N69u6Y9ODgYaWlp+OWXX151uBqcc0NERETFUiqVsLOz09pKqhJaWFigUaNG2LVrl6atoKAAu3btgkqlKq2QAch0WIqIiIhKX0hICIKDg9G4cWO8/vrr+OKLL/Dw4UMMHjy4VONgckNEREQG0adPH9y5cwczZ85EcnIy6tevj+3btxeZZPyqMbkhSSiVSsyaNYuTIIleAr9HVBaNHj0ao0ePljQGTigmIiIiWeGEYiIiIpIVJjdEREQkK0xuiHQQFhaG+vXrSx0GkeT27t0LhUKBtLQ0qUMhKhGTG5kYNGgQFAoF5s+fr9W+efNmKPR8QIinpye++OILnfopFAooFAqUK1cOfn5+WL58uV7XYtJAclH4HVQoFDA3N4eXlxc+/PBDZGVl6XQ8kwYiw2FyIyOWlpb45JNPcP/+/VK7Znh4OJKSknD27Fm8++67GD58OLZt21Zq1y8khEBeXl6pX5foSW+++SaSkpJw5coVLFy4EEuXLsWsWbNKPY7c3NxSvyZRWcLkRkYCAgLg6uqKiIiIZ/bbsGEDateuDaVSCU9PT3z++eeafa1bt8b169cxYcIEzW+hz2JrawtXV1dUrVoVU6ZMgaOjI2JjYzX709LSMGzYMDg5OcHOzg5t27bFqVOnAADR0dGYPXs2Tp06pblWdHQ0rl27BoVCgZMnT2qdR6FQYO/evQD+91vutm3b0KhRIyiVSuzfvx+tW7fG2LFj8eGHH8LR0RGurq5FnoHyrJgKzZ8/Hy4uLrC1tcXQoUN1/u2b/tuUSiVcXV1RuXJldO/eHQEBAZrvQ0FBASIiIuDl5QUrKyvUq1cP69evBwBcu3YNbdq0AQCUL18eCoUCgwYNAlB8JbV+/fpaP9cKhQLffPMNunbtCmtra3z88ceaqujq1avh6ekJe3t79O3bFw8ePNAc96yYCv3++++oUaMGrKys0KZNG1y7ds2wHxrRK8DkRkZMTU0xb948fPnll7hx40axfY4dO4bevXujb9++OHPmDMLCwjBjxgxER0cDADZu3IhKlSppKjJJSUk6XbugoAAbNmzA/fv3YWFhoWnv1asXbt++jW3btuHYsWNo2LAh2rVrh9TUVPTp0wcTJ05E7dq1Ndfq06ePXu956tSpmD9/Ps6fP4+6desCAGJiYmBtbY3Dhw8jMjIS4eHhWgnXs2ICgJ9//hlhYWGYN28ejh49Cjc3NyxZskSvuIjOnj2LgwcPar4PERER+O677xAVFYVz585hwoQJePfdd7Fv3z5UrlwZGzZsAABcuHABSUlJWLRokV7XCwsLw9tvv40zZ85gyJAhAIDLly9j8+bN2Lp1K7Zu3Yp9+/ZpDV0/KyYA+Pfff9GjRw906dIFJ0+exLBhwzB16lRDfDxEr5YgWQgODhbdunUTQgjRrFkzMWTIECGEEJs2bRJP/jH369dPtG/fXuvYyZMnC19fX81rDw8PsXDhwude08PDQ1hYWAhra2thZmYmAAhHR0eRkJAghBDizz//FHZ2diIrK0vruGrVqomlS5cKIYSYNWuWqFevntb+q1evCgDixIkTmrb79+8LAGLPnj1CCCH27NkjAIjNmzdrHduqVSvRokULrbYmTZqIKVOm6ByTSqUSH3zwgdb+pk2bFomT6EnBwcHC1NRUWFtbC6VSKQAIExMTsX79epGVlSXKlSsnDh48qHXM0KFDxTvvvCOE+N/P9P3797X6FPd9rFevnpg1a5bmNQAxfvx4rT6zZs0S5cqVExkZGZq2yZMni6ZNmwohhE4xhYaGav3dIIQQU6ZMKTZOorKEdyiWoU8++QRt27bFpEmTiuw7f/48unXrptXm7++PL774Avn5+TA1NdXrWpMnT8agQYOQlJSEyZMn44MPPoC3tzcA4NSpU8jMzESFChW0jnn8+DEuX76s57sqXuPGjYu0FVZwCrm5ueH27ds6x3T+/HmMGDFCa79KpcKePXsMEjPJV5s2bfDNN9/g4cOHWLhwIczMzBAUFIRz587h0aNHaN++vVb/nJwcNGjQwCDXLu674OnpCVtbW83rJ78Lly5dem5M58+fR9OmTbX2l/YDEIleBJMbGWrZsiUCAwMRGhqqGbd/VSpWrAhvb294e3tj3bp18PPzQ+PGjeHr64vMzEy4ublp5sk8ycHBocRzmpioR0vFEzfPLmmCpLW1dZE2c3NzrdcKhQIFBQUA8MIxEenC2tpak9yvXLkS9erVw4oVK1CnTh0AwG+//YbXXntN65jnPTrBxMRE67sAFP99eJHvwovGRFTWMbmRqfnz56N+/fqoWbOmVruPjw8OHDig1XbgwAHUqFFDU7WxsLBAfn6+3tesXLky+vTpg9DQUPzyyy9o2LAhkpOTYWZmBk9Pz2KPKe5aTk5OAICkpCTNb5BPTi5+GbrE5OPjg8OHD2PgwIGatkOHDhnk+vTfYWJigmnTpiEkJAQXL16EUqlEYmIiWrVqVWz/wrk5xX0fnpz7lpGRgatXr750fL6+vs+NycfHB1u2bNFq43eBjAEnFMuUn58f+vfvj8WLF2u1T5w4Ebt27cKcOXNw8eJFxMTE4KuvvtIawvL09ERcXBxu3ryJu3fv6nXdcePG4ddff8XRo0cREBAAlUqF7t27448//sC1a9dw8OBBfPTRRzh69KjmWlevXsXJkydx9+5dZGdnw8rKCs2aNdNMFN63bx+mT5/+8h8KoFNM48aNw8qVK7Fq1SpcvHgRs2bNwrlz5wxyffpv6dWrF0xNTbF06VJMmjQJEyZMQExMDC5fvozjx4/jyy+/RExMDADAw8MDCoUCW7duxZ07dzSVlbZt22L16tX4888/cebMGQQHB+s9fFwcW1vb58Y0YsQIJCQkYPLkybhw4QLWrl2rWXxAVKZJPemHDOPJCcWFrl69KiwsLMTTf8zr168Xvr6+wtzcXFSpUkV8+umnWvvj4+NF3bp1NZMiS1LSxOPAwEDRsWNHIYQQGRkZYsyYMcLd3V2Ym5uLypUri/79+4vExEQhhHpSY1BQkHBwcBAAxKpVq4QQQvz9999CpVIJKysrUb9+ffHHH38UO6H46UmNrVq1EuPGjdNq69atmwgODta8fl5MQgjx8ccfi4oVKwobGxsRHBwsPvzwQ04opmcq7jsohBARERHCyclJZGZmii+++ELUrFlTmJubCycnJxEYGCj27dun6RseHi5cXV2FQqHQ/Mymp6eLPn36CDs7O1G5cmURHR1d7ITiTZs2aV23uMn6CxcuFB4eHprXBQUFz43p119/Fd7e3kKpVIo33nhDrFy5khOKqczjU8GJiIhIVjgsRURERLLC5IaIiIhkhckNERERyQqTGyIiIpIVJjdEREQkK0xuiIiISFaY3BAREZGsMLkhIiIiWWFyQ0QAgEGDBqF79+6a161bt8b48eNLPY69e/dCoVAgLS2t1K9NRPLA5IaojBs0aBAUCgUUCgUsLCzg7e2N8PBw5OXlvdLrbty4EXPmzNGpLxMSIipL+FRwIiPw5ptvYtWqVcjOzsbvv/+OUaNGwdzcHKGhoVr9cnJyNE+XflmOjo4GOQ8RUWlj5YbICCiVSri6usLDwwMjR45EQEAAtmzZohlK+vjjj+Hu7o6aNWsCAP7991/07t0bDg4OcHR0RLdu3XDt2jXN+fLz8xESEgIHBwdUqFABH374IZ5+zNzTw1LZ2dmYMmUKKleuDKVSCW9vb6xYsQLXrl1DmzZtAADly5eHQqHAoEGDAAAFBQWIiIiAl5cXrKysUK9ePaxfv17rOr///jtq1KgBKysrtGnTRitOIqIXweSGyAhZWVkhJycHALBr1y5cuHABsbGx2Lp1K3JzcxEYGAhbW1v8+eefOHDgAGxsbPDmm29qjvn8888RHR2NlStXYv/+/UhNTcWmTZueec2BAwfihx9+wOLFi3H+/HksXboUNjY2qFy5MjZs2AAAuHDhApKSkrBo0SIAQEREBL777jtERUXh3LlzmDBhAt59913s27cPgDoJ69GjB7p06YKTJ09i2LBhmDp16qv62Ijov0Lip5IT0XMEBweLbt26CSGEKCgoELGxsUKpVIpJkyaJ4OBg4eLiIrKzszX9V69eLWrWrCkKCgo0bdnZ2cLKykrs2LFDCCGEm5ubiIyM1OzPzc0VlSpV0lxHCCFatWolxo0bJ4QQ4sKFCwKAiI2NLTbGPXv2CADi/v37mrasrCxRrlw5cfDgQa2+Q4cOFe+8844QQojQ0FDh6+urtX/KlClFzkVEpA/OuSEyAlu3boWNjQ1yc3NRUFCAfv36ISwsDKNGjYKfn5/WPJtTp07h0qVLsLW11TpHVlYWLl++jPT0dCQlJaFp06aafWZmZmjcuHGRoalCJ0+ehKmpKVq1aqVzzJcuXcKjR4/Qvn17rfacnBw0aNAAAHD+/HmtOABApVLpfA0iouIwuSEyAm3atME333wDCwsLuLu7w8zsf19da2trrb6ZmZlo1KgR1qxZU+Q8Tk5OL3R9KysrvY/JzMwEAPz222947bXXtPYplcoXioOISBdMboiMgLW1Nby9vXXq27BhQ/z0009wdnaGnZ1dsX3c3Nxw+PBhtGzZEgCQl5eHY8eOoWHDhsX29/PzQ0FBAfbt24eAgIAi+wsrR/n5+Zo2X19fKJVKJCYmlljx8fHxwZYtW7TaDh069Pw3SUT0DJxQTCQz/fv3R8WKFdGtWzf8+eefuHr1Kvbu3YuxY8fixo0bAIBx48Zh/vz52Lx5M/755x988MEHz7xHjaenJ4KDgzFkyBBs3rxZc86ff/4ZAODh4QGFQoGtW7fizp07yMzMhK2tLSZNmoQJEyYgJiYGly9fxvHjx/Hll18iJiYGADBixAgkJCRg8uTJuHDhAtauXYvo6OhX/RERkcwxuSGSmXLlyiEuLg5VqlRBjx494OPjg6FDhyIrK0tTyZk4cSIGDBiA4OBgqFQq2Nra4u23337meb/55hv07NkTH3zwAWrVqoXhw4fj4cOHAIDXXnsNs2fPxtSpU+Hi4oLRo0cDAObMmYMZM2YgIiICPj4+ePPNN/Hbb7/By8sLAFClShVs2LABmzdvRr169RAVFYV58+a9wk+HiP4LFKKkGYRERERERoiVGyIiIpIVJjdEREQkK0xuiIiISFaY3BAREZGsMLkhIiIiWWFyQ0RERLLC5IaIiIhkhckNERERyQqTGyIiIpIVJjdEREQkK0xuiIiISFaY3BAREZGs/B9CbyDVJbTqnAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tn, fp, fn, tp = cm.ravel()\n",
        "\n",
        "print(\"True Negative :\", tn)\n",
        "print(\"False Positive:\", fp)\n",
        "print(\"False Negative:\", fn)\n",
        "print(\"True Positive  :\", tp)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eITHX3S1mpVV",
        "outputId": "68f44db5-54f5-4594-cac9-f3181cf11ba6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True Negative : 710\n",
            "False Positive: 0\n",
            "False Negative: 0\n",
            "True Positive  : 290\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "coefficients = pd.DataFrame({\n",
        "    'Feature': features,\n",
        "    'Coefficient': model.coef_[0]\n",
        "})\n",
        "\n",
        "coefficients['Absolute_Coefficient'] = coefficients['Coefficient'].abs()\n",
        "\n",
        "coefficients = coefficients.sort_values(\n",
        "    by='Absolute_Coefficient',\n",
        "    ascending=False\n",
        ")\n",
        "\n",
        "print(coefficients)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3DHFOMVbmr93",
        "outputId": "675a2cf0-1210-4612-9644-c13ddc94cc1c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             Feature  Coefficient  Absolute_Coefficient\n",
            "6        Return_Cost     4.924540              4.924540\n",
            "4     Days_to_Return     2.101506              2.101506\n",
            "7        Profit_Loss    -0.151220              0.151220\n",
            "5        Order_Value     0.092233              0.092233\n",
            "2   Discount_Applied     0.064216              0.064216\n",
            "0      Product_Price     0.036622              0.036622\n",
            "12     High_Discount    -0.026095              0.026095\n",
            "11       Order_Month    -0.023516              0.023516\n",
            "10        Order_Year     0.014703              0.014703\n",
            "9    Packaging_Waste     0.006414              0.006414\n",
            "1     Order_Quantity     0.006414              0.006414\n",
            "8      CO2_Emissions     0.002619              0.002619\n",
            "3           User_Age     0.002327              0.002327\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "coefficients.sort_values('Coefficient')['Coefficient'].plot(kind='barh')\n",
        "\n",
        "plt.title('Logistic Regression Feature Coefficients')\n",
        "plt.xlabel('Coefficient')\n",
        "plt.ylabel('Feature')\n",
        "plt.tight_layout()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 607
        },
        "id": "-UKzx-4imw9k",
        "outputId": "cc324cc2-f19b-489b-d585-466f4f02c4dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAST5JREFUeJzt3Xm8l3P+P/7nW+lUp85JtEinVUSUZJkUQvRJGmYYpKGyzBhZs9XXR8vI1DAzYiTrp+zMoBjGmm0WRkk+2VKmCGXvnJbp0On6/eHX++PoVKecq/ep7vfb7brdXMv7fT3O1XXw6HUtmSRJkgAAAACq3Da5DgAAAABbKqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRtgK9WjR4/o0aNHlX1fq1atYuDAgVX2fURkMpkYOXJkrmNQDdx5553Rvn372HbbbaNBgwbZ5VdffXW0adMmatSoEXvttVdEbNzv4vz58yOTycSkSZOqLDMA31K6AXJs0qRJkclkYvr06bmOsl7//Oc/Y+TIkbF48eJU99OqVavIZDLZKT8/P/bbb7+44447Ut0v3xo5cmS54//d6cYbb0xln3/961+r/V8wzJw5M37+859HUVFR5OXlRcOGDaNnz54xceLEKCsrS22/77zzTgwcODDatm0bt9xyS9x8880REfHUU0/FJZdcEt26dYuJEyfGb37zm9QyVJUbbrhBsQe2OjVzHQCA3Hjqqac2+DP//Oc/Y9SoUTFw4MByo20REbNnz45ttqm6v8vda6+94sILL4yIiIULF8att94aAwYMiNLS0jjjjDOqbD/V2X/+85+oWTN3/6meMGFC1KtXr9yy/fffP5V9/fWvf43x48dX2+J96623xplnnhlNmjSJk08+Odq1axdLliyJqVOnxmmnnRYLFy6M//f//l8q+37++edj1apVce2118bOO++cXf7ss8/GNttsE7fddlvUqlUru3xjfhdbtmwZ//nPf2LbbbetstwVueGGG2KHHXZwVQywVVG6AbZS3/2f9KqQl5dXpd+30047xc9//vPs/MCBA6NNmzZxzTXXbPLSvWzZssjPz9+k+4yIqF279ibf53cdd9xxscMOO+Q0ww9VFX92L7/8cpx55pnRtWvX+Otf/xr169fPrjv//PNj+vTp8cYbb/zQqGv16aefRkSs8Rddn376adSpU2eN3+WN+V3MZDI5P98AtlQuLwfYTLz22mvRu3fvKCgoiHr16sVhhx0WL7/88hrb/e///m8cfPDBUadOnWjevHmMHj06Jk6cGJlMJubPn5/drqJ7uv/4xz9Ghw4dom7durHddtvFPvvsE/fcc09EfHvJ8cUXXxwREa1bt85ebrz6Oyu6j3Tx4sVxwQUXRKtWrSIvLy+aN28ep5xySnz++ecb/PM3atQo2rdvH++991655atWrYpx48ZFhw4donbt2tGkSZP45S9/GV999dUa240cOTKaNWsWdevWjUMOOSTeeuutNXKvvtz/hRdeiLPOOisaN24czZs3z65//PHH48ADD4z8/PyoX79+9OnTJ958881y+1q0aFEMGjQomjdvHnl5ebHjjjvG0UcfXe74T58+PXr16hU77LBD1KlTJ1q3bh2nnnpque+p6J7uypwHq3+Gf/zjHzFkyJBo1KhR5Ofnx09+8pP47LPPKnvI1+uuu+6KLl26RJ06daJhw4Zx4oknxoIFC8pt87e//S1+9rOfRYsWLSIvLy+KioriggsuiP/85z/ZbQYOHBjjx4/P/syrp4hvR3kzmUw8//zz5b63onuQBw4cGPXq1Yv33nsvjjzyyKhfv370798/Iip/nlRk1KhRkclk4u677y5XuFfbZ599yp1Dy5YtiwsvvDB7Gfquu+4av/vd7yJJkg0+hq1atYoRI0ZExLe/A6vPiUwmExMnToxly5Zlj9fqY7Exv4tru6f7nXfeieOOOy4aNmwYtWvXjn322SceeeSRcttU9nxr1apVvPnmm/HCCy9kM6/+d9A333wTo0aNinbt2kXt2rVj++23j+7du8fTTz+9zj8bgM2BkW6AzcCbb74ZBx54YBQUFMQll1wS2267bdx0003Ro0ePeOGFF7KX/H700UdxyCGHRCaTiWHDhkV+fn7ceuutlRr5uuWWW+Lcc8+N4447Ls4777xYsWJF/O///m/861//ipNOOil++tOfxrvvvhv33ntvXHPNNdkR0EaNGlX4fUuXLo0DDzww3n777Tj11FNj7733js8//zweeeSR+PDDDzd4BHXlypXx4YcfxnbbbVdu+S9/+cuYNGlSDBo0KM4999yYN29eXH/99fHaa6/FP/7xj+zlssOGDYurrroq+vbtG7169YrXX389evXqFStWrKhwf2eddVY0atQohg8fHsuWLYuIbx9mNWDAgOjVq1f89re/jeXLl8eECROie/fu8dprr0WrVq0iIuLYY4+NN998M84555xo1apVfPrpp/H000/HBx98kJ0/4ogjolGjRjF06NBo0KBBzJ8/Px566KF1HoPKngernXPOObHddtvFiBEjYv78+TFu3Lg4++yz4/7776/UMf/yyy/LzdeoUSN7/K+88sq4/PLL4/jjj4/TTz89Pvvss/jjH/8YBx10ULz22mvZUdk///nPsXz58vjVr34V22+/fbzyyivxxz/+MT788MP485//nP0z/Pjjj+Ppp5+OO++8s1LZ1mblypXRq1ev6N69e/zud7+LunXrZvdRmfPk+5YvXx5Tp06Ngw46KFq0aLHe/SdJEj/+8Y/jueeei9NOOy322muvePLJJ+Piiy+Ojz76KK655prstpU5huPGjYs77rgjJk+enL3cv2PHjrHzzjvHzTffHK+88krceuutERFxwAEHVJhpY38X33zzzejWrVvstNNOMXTo0MjPz48//elPccwxx8SDDz4YP/nJT8ptv77zbdy4cXHOOedEvXr14rLLLouIiCZNmkTEt3+pN2bMmDj99NNjv/32i5KSkpg+fXrMmDEjDj/88PUed4BqLQEgpyZOnJhERDJt2rS1bnPMMccktWrVSt57773sso8//jipX79+ctBBB2WXnXPOOUkmk0lee+217LIvvvgiadiwYRIRybx587LLDz744OTggw/Ozh999NFJhw4d1pn16quvXuN7VmvZsmUyYMCA7Pzw4cOTiEgeeuihNbZdtWrVOvfTsmXL5Igjjkg+++yz5LPPPktmzZqVnHzyyUlEJIMHD85u97e//S2JiOTuu+8u9/knnnii3PJFixYlNWvWTI455phy240cOTKJiHK5V/95dO/ePVm5cmV2+ZIlS5IGDRokZ5xxRrnvWLRoUVJYWJhd/tVXXyURkVx99dVr/fkmT5683j/zJEmSiEhGjBiRna/sebD6Z+jZs2e5Y33BBRckNWrUSBYvXrzO/Y4YMSKJiDWmli1bJkmSJPPnz09q1KiRXHnlleU+N2vWrKRmzZrlli9fvnyN7x8zZkySyWSS999/P7ts8ODBSUX/W/Lcc88lEZE899xz5ZbPmzcviYhk4sSJ2WUDBgxIIiIZOnRouW0re55U5PXXX08iIjnvvPPWus13TZkyJYmIZPTo0eWWH3fccUkmk0nmzp2bJMmGHcPVfx6fffZZuW0HDBiQ5Ofnr5FhY34XKzqehx12WLLnnnsmK1asKLf9AQcckLRr1y67bEPOtw4dOpT7985qnTp1Svr06bPGcoAtgcvLAaq5srKyeOqpp+KYY46JNm3aZJfvuOOOcdJJJ8Xf//73KCkpiYiIJ554Irp27Zp9dVBERMOGDbOX2K5LgwYN4sMPP4xp06ZVSe4HH3wwOnXqtMZoWERkLx1el6eeeioaNWoUjRo1ij333DPuvPPOGDRoUFx99dXZbf785z9HYWFhHH744fH5559npy5dukS9evXiueeei4iIqVOnxsqVK+Oss84qt49zzjlnrfs/44wzokaNGtn5p59+OhYvXhz9+vUrt68aNWrE/vvvn93X6ntsn3/++bVeurx6FPjRRx+Nb775Zr3HImLDzoPVfvGLX5Q71gceeGCUlZXF+++/X6l9Pvjgg/H0009np7vvvjsiIh566KFYtWpVHH/88eWORdOmTaNdu3bZY7H6eKy2bNmy+Pzzz+OAAw6IJEnitddeq1SODfWrX/2q3Hxlz5OKrD6mFV1WXpG//vWvUaNGjTj33HPLLb/wwgsjSZJ4/PHHI2LDjuEPtTG/i19++WU8++yzcfzxx8eSJUuy+b744ovo1atXzJkzJz766KNyn/kh51uDBg3izTffjDlz5mzgTwdQ/bm8HKCa++yzz2L58uWx6667rrFut912i1WrVsWCBQuiQ4cO8f7770fXrl3X2O67Tzxem0svvTSeeeaZ2G+//WLnnXeOI444Ik466aTo1q3bRuV+77334thjj92oz0Z8+5Ts0aNHR1lZWbzxxhsxevTo+Oqrr8o9NGrOnDlRXFwcjRs3rvA7Vj+AavX/9H//ODRs2HCNy9VXa926dbn51WXg0EMPrXD7goKCiPj2IVa//e1v48ILL4wmTZrEj370ozjqqKPilFNOiaZNm0ZExMEHHxzHHntsjBo1Kq655pro0aNHHHPMMXHSSSet9VaADTkPVvv+5dCrf9bK3MccEXHQQQdVeOnxnDlzIkmSaNeuXYWf++6l2h988EEMHz48HnnkkTX2W1xcXKkcG6JmzZrl7sFfnbcy50lFVv+5LlmypFL7f//996NZs2ZrlPTddtstu351psoewx9qY34X586dG0mSxOWXXx6XX355hdt8+umnsdNOO2Xnf8j59utf/zqOPvro2GWXXWKPPfaI//qv/4qTTz45OnbsuEG5AaojpRuAiPi2FMyePTseffTReOKJJ+LBBx+MG264IYYPHx6jRo3a5Hl22GGH6NmzZ0RE9OrVK9q3bx9HHXVUXHvttTFkyJCI+PbhWI0bN86OwH7f2u43r4zvjtCu3lfEt/d1ry7P3/XdV3udf/750bdv35gyZUo8+eSTcfnll8eYMWPi2Wefjc6dO0cmk4kHHnggXn755fjLX/4STz75ZJx66qnx+9//Pl5++eU1XtO1sb47Uv9dSQUP9NoQq1atikwmE48//niF+1idv6ysLA4//PD48ssv49JLL4327dtHfn5+fPTRRzFw4MDsMV2XtY3Eru292Hl5eWu8LuuHnCc777xz1KxZM2bNmrXerBuisscwV1b/2Vx00UXRq1evCrf5/l9i/ZDz7aCDDor33nsvHn744Xjqqafi1ltvjWuuuSZuvPHGOP300zcwPUD1onQDVHONGjWKunXrxuzZs9dY984778Q222wTRUVFEfHtu3bnzp27xnYVLatIfn5+nHDCCXHCCSfE119/HT/96U/jyiuvjGHDhkXt2rUrdVn4am3btq3S1yj16dMnDj744PjNb34Tv/zlLyM/Pz/atm0bzzzzTHTr1m2NkvxdLVu2jIhvj8N3R7C/+OKLSo/6tm3bNiIiGjdunP3LgPVtf+GFF8aFF14Yc+bMib322it+//vfx1133ZXd5kc/+lH86Ec/iiuvvDLuueee6N+/f9x3330VlowNOQ/S1rZt20iSJFq3bh277LLLWrebNWtWvPvuu3H77bfHKaeckl1e0ROp13ZurR4tXbx4cbnllb1EfnXeypwnFalbt24ceuih8eyzz8aCBQvWe4xbtmwZzzzzTCxZsqTcaPc777yTXb86U2WOYVXYmN/F1bcwbLvttpU63ytrXf8OadiwYQwaNCgGDRoUS5cujYMOOihGjhypdAObPfd0A1RzNWrUiCOOOCIefvjhcq+c+uSTT+Kee+6J7t27Zy+B7dWrV7z00ksxc+bM7HZffvnlWkf4vuuLL74oN1+rVq3YfffdI0mS7H3Hq993/P0CVJFjjz02Xn/99Zg8efIa6zZ2pPXSSy+NL774Im655ZaIiDj++OOjrKwsrrjiijW2XblyZTbnYYcdFjVr1owJEyaU2+b666+v9L579eoVBQUF8Zvf/KbC+7BXvxpp+fLlazwRvW3btlG/fv0oLS2NiG8vt/3+MVh9H/7qbb5vQ86DtP30pz+NGjVqxKhRo9b4OZIkyZ5Lq0c+v7tNkiRx7bXXrvGdazu3WrZsGTVq1IgXX3yx3PIbbrih0nkre56szYgRIyJJkjj55JNj6dKla6x/9dVX4/bbb4+IiCOPPDLKysrWOLeuueaayGQy0bt374io/DGsChvzu9i4cePo0aNH3HTTTbFw4cI11m/sq+fy8/MrPN7f/3nr1asXO++881p/HwA2J0a6AaqJ//mf/4knnnhijeXnnXdejB49Op5++uno3r17nHXWWVGzZs246aaborS0NK666qrstpdcckncddddcfjhh8c555yTfWVYixYt4ssvv1znKNMRRxwRTZs2jW7dukWTJk3i7bffjuuvvz769OmTHbHr0qVLRERcdtllceKJJ8a2224bffv2zRam77r44ovjgQceiJ/97Gdx6qmnRpcuXeLLL7+MRx55JG688cbo1KnTBh+j3r17xx577BF/+MMfYvDgwXHwwQfHL3/5yxgzZkzMnDkzjjjiiNh2221jzpw58ec//zmuvfbaOO6446JJkyZx3nnnxe9///v48Y9/HP/1X/8Vr7/+ejz++OOxww47VGoEv6CgICZMmBAnn3xy7L333nHiiSdGo0aN4oMPPojHHnssunXrFtdff328++67cdhhh8Xxxx8fu+++e9SsWTMmT54cn3zySZx44okREXH77bfHDTfcED/5yU+ibdu2sWTJkrjllluioKAgjjzyyLVmqOx5kLa2bdvG6NGjY9iwYTF//vw45phjon79+jFv3ryYPHly/OIXv4iLLroo2rdvH23bto2LLrooPvrooygoKIgHH3ywwqsLVp9b5557bvTq1Stq1KgRJ554YhQWFsbPfvaz+OMf/xiZTCbatm0bjz766Drvw/6+yp4na3PAAQfE+PHj46yzzor27dvHySefHO3atYslS5bE888/H4888kiMHj06IiL69u0bhxxySFx22WUxf/786NSpUzz11FPx8MMPx/nnn5+9YqKyx7AqbOzv4vjx46N79+6x5557xhlnnBFt2rSJTz75JF566aX48MMP4/XXX9/gLF26dIkJEybE6NGjY+edd47GjRvHoYceGrvvvnv06NEjunTpEg0bNozp06fHAw88EGefffYP/fEBcm/TPiwdgO9b/bqdtU0LFixIkiRJZsyYkfTq1SupV69eUrdu3eSQQw5J/vnPf67xfa+99lpy4IEHJnl5eUnz5s2TMWPGJNddd10SEcmiRYuy233/lWE33XRTctBBByXbb799kpeXl7Rt2za5+OKLk+Li4nLff8UVVyQ77bRTss0225R7fdj3X1OUJN++ruzss89Odtppp6RWrVpJ8+bNkwEDBiSff/75Oo9Jy5Yt1/r6oEmTJq3xaqObb7456dKlS1KnTp2kfv36yZ577plccsklyccff5zdZuXKlcnll1+eNG3aNKlTp05y6KGHJm+//Xay/fbbJ2eeeeYafx5re53Xc889l/Tq1SspLCxMateunbRt2zYZOHBgMn369CRJkuTzzz9PBg8enLRv3z7Jz89PCgsLk/333z/505/+lP2OGTNmJP369UtatGiR5OXlJY0bN06OOuqo7HesFt97Zdjqz67vPFjbz7C2129939peUfV9Dz74YNK9e/ckPz8/yc/PT9q3b58MHjw4mT17dnabt956K+nZs2dSr169ZIcddkjOOOOM7Gu4vvtnuHLlyuScc85JGjVqlGQymXKvD/vss8+SY489Nqlbt26y3XbbJb/85S+TN954o8JXhlX0Cq3VKnOerMurr76anHTSSUmzZs2SbbfdNtluu+2Sww47LLn99tuTsrKy7HZLlixJLrjggux27dq1S66++uoKX5VXmWP4Q18ZliTr/12s6JVhSZIk7733XnLKKackTZs2Tbbddttkp512So466qjkgQceyG6zIefbokWLkj59+iT169dPIiL776DRo0cn++23X9KgQYOkTp06Sfv27ZMrr7wy+frrr9f8gwDYzGSS5Ac+TQWAau/888+Pm266KZYuXbrWhx1tjRYvXhzbbbddjB49Oi677LJcxwEAtkDu6QbYwvznP/8pN//FF1/EnXfeGd27d9+qC/f3j0tExLhx4yIiokePHps2DACw1XBPN8AWpmvXrtGjR4/Ybbfd4pNPPonbbrstSkpK1vqu3a3F/fffH5MmTYojjzwy6tWrF3//+9/j3nvvjSOOOGKj30UOALA+SjfAFubII4+MBx54IG6++ebIZDKx9957x2233RYHHXRQrqPlVMeOHaNmzZpx1VVXRUlJSfbhaqsfgAUAkAb3dAMAAEBK3NMNAAAAKVG6AQAAICVb/D3dq1atio8//jjq168fmUwm13EAAADYAiRJEkuWLIlmzZrFNtusfTx7iy/dH3/8cRQVFeU6BgAAAFugBQsWRPPmzde6fosv3fXr14+Ibw9EQUFBjtMAAACwJSgpKYmioqJs51ybLb50r76kvKCgQOkGAACgSq3vNmYPUgMAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJVv8e7opr9XQx3IdAQAAYJ3mj+2T6whVxkg3AAAApETpBgAAgJQo3QAAAJASpRsAAABSUu1L90cffRQ///nPY/vtt486derEnnvuGdOnT891LAAAAFivav308q+++iq6desWhxxySDz++OPRqFGjmDNnTmy33Xa5jgYAAADrVa1L929/+9soKiqKiRMnZpe1bt06h4kAAACg8qr15eWPPPJI7LPPPvGzn/0sGjduHJ07d45bbrkl17EAAACgUqp16f73v/8dEyZMiHbt2sWTTz4Zv/rVr+Lcc8+N22+/fa2fKS0tjZKSknITAAAA5EK1vrx81apVsc8++8RvfvObiIjo3LlzvPHGG3HjjTfGgAEDKvzMmDFjYtSoUZsyJgAAAFSoWo9077jjjrH77ruXW7bbbrvFBx98sNbPDBs2LIqLi7PTggUL0o4JAAAAFarWI93dunWL2bNnl1v27rvvRsuWLdf6mby8vMjLy0s7GgAAAKxXtR7pvuCCC+Lll1+O3/zmNzF37ty455574uabb47BgwfnOhoAAACsV7Uu3fvuu29Mnjw57r333thjjz3iiiuuiHHjxkX//v1zHQ0AAADWq1pfXh4RcdRRR8VRRx2V6xgAAACwwar1SDcAAABszpRuAAAASInSDQAAACmp9vd0U7Xmj+2T6wgAAABbDSPdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASmrmOgCbVquhj+U6AsAWb/7YPrmOAABUE0a6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQks2qdI8dOzYymUycf/75uY4CAAAA67XZlO5p06bFTTfdFB07dsx1FAAAAKiUzaJ0L126NPr37x+33HJLbLfddrmOAwAAAJWyWZTuwYMHR58+faJnz565jgIAAACVVjPXAdbnvvvuixkzZsS0adMqtX1paWmUlpZm50tKStKKBgAAAOtUrUe6FyxYEOedd17cfffdUbt27Up9ZsyYMVFYWJidioqKUk4JAAAAFcskSZLkOsTaTJkyJX7yk59EjRo1ssvKysoik8nENttsE6WlpeXWRVQ80l1UVBTFxcVRUFCwybJXV62GPpbrCABbvPlj++Q6AgCQspKSkigsLFxv16zWl5cfdthhMWvWrHLLBg0aFO3bt49LL710jcIdEZGXlxd5eXmbKiIAAACsVbUu3fXr14899tij3LL8/PzYfvvt11gOAAAA1U21vqcbAAAANmfVeqS7Is8//3yuIwAAAEClGOkGAACAlCjdAAAAkBKlGwAAAFKy2d3TzQ/j3bEAAACbjpFuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJTVzHYBNq9XQxzb6s/PH9qnCJAAAAFs+I90AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEhJtS/dI0eOjEwmU25q3759rmMBAADAem0WTy/v0KFDPPPMM9n5mjU3i9gAAABs5TaL9lqzZs1o2rRprmMAAADABqn2l5dHRMyZMyeaNWsWbdq0if79+8cHH3yw1m1LS0ujpKSk3AQAAAC5UO1L9/777x+TJk2KJ554IiZMmBDz5s2LAw88MJYsWVLh9mPGjInCwsLsVFRUtIkTAwAAwLcySZIkuQ6xIRYvXhwtW7aMP/zhD3Haaaetsb60tDRKS0uz8yUlJVFUVBTFxcVRUFCwKaNWS62GPrbRn50/tk8VJgEAANh8lZSURGFh4Xq75mZxT/d3NWjQIHbZZZeYO3duhevz8vIiLy9vE6cCAACANVX7y8u/b+nSpfHee+/FjjvumOsoAAAAsE7VvnRfdNFF8cILL8T8+fPjn//8Z/zkJz+JGjVqRL9+/XIdDQAAANap2l9e/uGHH0a/fv3iiy++iEaNGkX37t3j5ZdfjkaNGuU6GgAAAKxTtS/d9913X64jAAAAwEap9peXAwAAwOZK6QYAAICUKN0AAACQkmp/TzdVa/7YPrmOAAAAsNUw0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICU1cx2ATavV0Mcqve38sX1STAIAALDlM9INAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQkmpfuseMGRP77rtv1K9fPxo3bhzHHHNMzJ49O9exAAAAYL2qfel+4YUXYvDgwfHyyy/H008/Hd98800cccQRsWzZslxHAwAAgHWq9u/pfuKJJ8rNT5o0KRo3bhyvvvpqHHTQQTlKBQAAAOtX7Uv39xUXF0dERMOGDStcX1paGqWlpdn5kpKSTZILAAAAvq/aX17+XatWrYrzzz8/unXrFnvssUeF24wZMyYKCwuzU1FR0SZOCQAAAN/arEr34MGD44033oj77rtvrdsMGzYsiouLs9OCBQs2YUIAAAD4P5vN5eVnn312PProo/Hiiy9G8+bN17pdXl5e5OXlbcJkAAAAULFqX7qTJIlzzjknJk+eHM8//3y0bt0615EAAACgUqp96R48eHDcc8898fDDD0f9+vVj0aJFERFRWFgYderUyXE6AAAAWLtqf0/3hAkTori4OHr06BE77rhjdrr//vtzHQ0AAADWqdqPdCdJkusIAAAAsFGq/Ug3AAAAbK6UbgAAAEiJ0g0AAAApqfb3dFO15o/tk+sIAAAAWw0j3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUlIz1wHYtFoNfazC5fPH9tnESQAAALZ8RroBAAAgJUo3AAAApETpBgAAgJQo3QAAAJCSzaJ0jx8/Plq1ahW1a9eO/fffP1555ZVcRwIAAID1qval+/77748hQ4bEiBEjYsaMGdGpU6fo1atXfPrpp7mOBgAAAOtU7Uv3H/7whzjjjDNi0KBBsfvuu8eNN94YdevWjf/5n//JdTQAAABYp2pdur/++ut49dVXo2fPntll22yzTfTs2TNeeumlHCYDAACA9auZ6wDr8vnnn0dZWVk0adKk3PImTZrEO++8U+FnSktLo7S0NDtfUlKSakYAAABYm2o90r0xxowZE4WFhdmpqKgo15EAAADYSlXr0r3DDjtEjRo14pNPPim3/JNPPommTZtW+Jlhw4ZFcXFxdlqwYMGmiAoAAABrqNalu1atWtGlS5eYOnVqdtmqVati6tSp0bVr1wo/k5eXFwUFBeUmAAAAyIVqfU93RMSQIUNiwIABsc8++8R+++0X48aNi2XLlsWgQYNyHQ0AAADWqdqX7hNOOCE+++yzGD58eCxatCj22muveOKJJ9Z4uBoAAABUN9W+dEdEnH322XH22WfnOgYAAABskGp9TzcAAABszpRuAAAASInSDQAAAClRugEAACAlm8WD1Kg688f2yXUEAACArYaRbgAAAEiJ0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6tzKthj4WrYY+lusYAAAAWwWlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKclp6X7xxRejb9++0axZs8hkMjFlypRy65MkieHDh8eOO+4YderUiZ49e8acOXNyExYAAAA2UE5L97Jly6JTp04xfvz4CtdfddVVcd1118WNN94Y//rXvyI/Pz969eoVK1as2MRJAQAAYMPVzOXOe/fuHb17965wXZIkMW7cuPjv//7vOProoyMi4o477ogmTZrElClT4sQTT9yUUQEAAGCDVdt7uufNmxeLFi2Knj17ZpcVFhbG/vvvHy+99FIOkwEAAEDl5HSke10WLVoUERFNmjQpt7xJkybZdRUpLS2N0tLS7HxJSUk6AQEAAGA9qu1I98YaM2ZMFBYWZqeioqJcRwIAAGArVW1Ld9OmTSMi4pNPPim3/JNPPsmuq8iwYcOiuLg4Oy1YsCDVnAAAALA21bZ0t27dOpo2bRpTp07NLispKYl//etf0bVr17V+Li8vLwoKCspNAAAAkAs5vad76dKlMXfu3Oz8vHnzYubMmdGwYcNo0aJFnH/++TF69Oho165dtG7dOi6//PJo1qxZHHPMMbkLDQAAAJWU09I9ffr0OOSQQ7LzQ4YMiYiIAQMGxKRJk+KSSy6JZcuWxS9+8YtYvHhxdO/ePZ544omoXbt2riIDAABApWWSJElyHSJNJSUlUVhYGMXFxS41j4hWQx+LiIj5Y/vkOAkAAMDmq7Jds9re0w0AAACbO6UbAAAAUqJ0AwAAQEpy+iA1Nj33cgMAAGw6RroBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASja6dN95553RrVu3aNasWbz//vsRETFu3Lh4+OGHqywcAAAAbM42qnRPmDAhhgwZEkceeWQsXrw4ysrKIiKiQYMGMW7cuKrMBwAAAJutjSrdf/zjH+OWW26Jyy67LGrUqJFdvs8++8SsWbOqLBwAAABszjaqdM+bNy86d+68xvK8vLxYtmzZDw4FAAAAW4KNKt2tW7eOmTNnrrH8iSeeiN122+2HZgIAAIAtQs2N+dCQIUNi8ODBsWLFikiSJF555ZW49957Y8yYMXHrrbdWdUYAAADYLG1U6T799NOjTp068d///d+xfPnyOOmkk6JZs2Zx7bXXxoknnljVGQEAAGCztMGle+XKlXHPPfdEr169on///rF8+fJYunRpNG7cOI18AAAAsNna4Hu6a9asGWeeeWasWLEiIiLq1q2rcAMAAEAFNupBavvtt1+89tprVZ0FAAAAtigbdU/3WWedFRdeeGF8+OGH0aVLl8jPzy+3vmPHjlUSDgAAADZnmSRJkg390DbbrDlAnslkIkmSyGQyUVZWViXhqkJJSUkUFhZGcXFxFBQU5DoOAAAAW4DKds2NGumeN2/eRgcDAACArcVGle6WLVtWdQ42kVZDH4v5Y/vkOgYAAMBWYaNK9x133LHO9aeccspGhQEAAIAtyUaV7vPOO6/c/DfffBPLly+PWrVqRd26dZVuAAAAiI18ZdhXX31Vblq6dGnMnj07unfvHvfee29VZwQAAIDN0kaV7oq0a9cuxo4du8YoOAAAAGytqqx0R0TUrFkzPv7446r8yliyZEmcf/750bJly6hTp04ccMABMW3atCrdBwAAAKRho+7pfuSRR8rNJ0kSCxcujOuvvz66detWJcFWO/300+ONN96IO++8M5o1axZ33XVX9OzZM956663YaaedqnRfAAAAUJUySZIkG/qhbbYpP0CeyWSiUaNGceihh8bvf//72HHHHask3H/+85+oX79+PPzww9Gnz/+95qpLly7Ru3fvGD169Hq/o7IvLN9aeGUYAADAD1fZrrlRI92rVq3a6GAbYuXKlVFWVha1a9cut7xOnTrx97//fZNkAAAAgI21Ufd0//rXv47ly5evsfw///lP/PrXv/7BoVarX79+dO3aNa644or4+OOPo6ysLO6666546aWXYuHChRV+prS0NEpKSspNAAAAkAsbVbpHjRoVS5cuXWP58uXLY9SoUT841HfdeeedkSRJ7LTTTpGXlxfXXXdd9OvXb41L3FcbM2ZMFBYWZqeioqIqzQMAAACVtVGlO0mSyGQyayx//fXXo2HDhj841He1bds2XnjhhVi6dGksWLAgXnnllfjmm2+iTZs2FW4/bNiwKC4uzk4LFiyo0jwAAABQWRt0T/d2220XmUwmMplM7LLLLuWKd1lZWSxdujTOPPPMKg8ZEZGfnx/5+fnx1VdfxZNPPhlXXXVVhdvl5eVFXl5eKhkAAABgQ2xQ6R43blwkSRKnnnpqjBo1KgoLC7PratWqFa1atYquXbtWacAnn3wykiSJXXfdNebOnRsXX3xxtG/fPgYNGlSl+wEAAICqtkGle8CAARER0bp16zjggANi2223TSXUdxUXF8ewYcPiww8/jIYNG8axxx4bV1555SbZNwAAAPwQG/XKsIMPPjj7zytWrIivv/663PqqfB/28ccfH8cff3yVfR8AAABsKhv1ILXly5fH2WefHY0bN478/PzYbrvtyk0AAADARpbuiy++OJ599tmYMGFC5OXlxa233hqjRo2KZs2axR133FHVGQEAAGCztFGXl//lL3+JO+64I3r06BGDBg2KAw88MHbeeedo2bJl3H333dG/f/+qzgkAAACbnY0a6f7yyy+z78kuKCiIL7/8MiIiunfvHi+++GLVpaPKzR/bJ9cRAAAAthobVbrbtGkT8+bNi4iI9u3bx5/+9KeI+HYEvEGDBlUWDgAAADZnG1W6Bw0aFK+//npERAwdOjTGjx8ftWvXjgsuuCAuvvjiKg0IAAAAm6tMkiTJD/2S999/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5MmTY/fdd69w29LS0igtLc3Ol5SUbKqYAAAAUE61v6c7ImLXXXeNmTNnxr/+9a/41a9+FQMGDIi33nqrwm3HjBkThYWF2amoqGgTpwUAAIBvbZb3dPfs2TPatm0bN9100xrrKhrpLioqck83AAAAVWaLvKd7tVWrVpUr1t+Vl5cXeXl5mzgRAAAArKnal+5hw4ZF7969o0WLFrFkyZK455574vnnn48nn3wy19EAAABgnap96f7000/jlFNOiYULF0ZhYWF07NgxnnzyyTj88MNzHQ0AAADWqdqX7ttuuy3XEQAAAGCjbBZPLwcAAIDNkdINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFJSM9cBSFeroY+Vm58/tk+OkgAAAGx9jHQDAABASpRuAAAASInSDQAAAClRugEAACAlOS3dL774YvTt2zeaNWsWmUwmpkyZUm79Qw89FEcccURsv/32kclkYubMmTnJCQAAABsjp6V72bJl0alTpxg/fvxa13fv3j1++9vfbuJkAAAA8MPl9JVhvXv3jt69e691/cknnxwREfPnz99EiQAAAKDquKcbAAAAUpLTke40lJaWRmlpaXa+pKQkh2kAAADYmm1xI91jxoyJwsLC7FRUVJTrSAAAAGyltrjSPWzYsCguLs5OCxYsyHUkAAAAtlJb3OXleXl5kZeXl+sYAAAAkNvSvXTp0pg7d252ft68eTFz5sxo2LBhtGjRIr788sv44IMP4uOPP46IiNmzZ0dERNOmTaNp06Y5yQwAAACVldPLy6dPnx6dO3eOzp07R0TEkCFDonPnzjF8+PCIiHjkkUeic+fO0adPn4iIOPHEE6Nz585x44035iwzAAAAVFZOR7p79OgRSZKsdf3AgQNj4MCBmy4QAAAAVKEt7kFqAAAAUF0o3QAAAJASpRsAAABSssW9Mozy5o/tk+sIAAAAWy0j3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAAACkROkGAACAlCjdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEpq5joA6Wo19LFy8/PH9slREgAAgK2PkW4AAABIidINAAAAKVG6AQAAICVKNwAAAKQkp6X7xRdfjL59+0azZs0ik8nElClTsuu++eabuPTSS2PPPfeM/Pz8aNasWZxyyinx8ccf5y4wAAAAbICclu5ly5ZFp06dYvz48WusW758ecyYMSMuv/zymDFjRjz00EMxe/bs+PGPf5yDpAAAALDhcvrKsN69e0fv3r0rXFdYWBhPP/10uWXXX3997LfffvHBBx9EixYtNkVEAAAA2Gib1T3dxcXFkclkokGDBrmOAgAAAOuV05HuDbFixYq49NJLo1+/flFQULDW7UpLS6O0tDQ7X1JSsiniAQAAwBo2i5Hub775Jo4//vhIkiQmTJiwzm3HjBkThYWF2amoqGgTpQQAAIDyqn3pXl2433///Xj66afXOcodETFs2LAoLi7OTgsWLNhESQEAAKC8an15+erCPWfOnHjuuedi++23X+9n8vLyIi8vbxOkAwAAgHXLaeleunRpzJ07Nzs/b968mDlzZjRs2DB23HHHOO6442LGjBnx6KOPRllZWSxatCgiIho2bBi1atXKVWwAAAColJyW7unTp8chhxySnR8yZEhERAwYMCBGjhwZjzzySERE7LXXXuU+99xzz0WPHj02VUwAAADYKDkt3T169IgkSda6fl3rAAAAoLqr9g9SAwAAgM2V0g0AAAApUboBAAAgJdX6lWH8cPPH9sl1BAAAgK2WkW4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJUo3AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlNXMdgP/Tauhjqe9j/tg+qe8DAACAbxnpBgAAgJQo3QAAAJASpRsAAABSonQDAABASqp96W7VqlVkMpk1psGDB+c6GgAAAKxTtX96+bRp06KsrCw7/8Ybb8Thhx8eP/vZz3KYCgAAANav2pfuRo0alZsfO3ZstG3bNg4++OAcJQIAAIDKqfal+7u+/vrruOuuu2LIkCGRyWQq3Ka0tDRKS0uz8yUlJZsqHgAAAJRT7e/p/q4pU6bE4sWLY+DAgWvdZsyYMVFYWJidioqKNl1AAAAA+I7NqnTfdttt0bt372jWrNlatxk2bFgUFxdnpwULFmzChAAAAPB/NpvLy99///145pln4qGHHlrndnl5eZGXl7eJUgEAAMDabTYj3RMnTozGjRtHnz59ch0FAAAAKmWzKN2rVq2KiRMnxoABA6Jmzc1mcB4AAICt3GZRup955pn44IMP4tRTT811FAAAAKi0zWLY+IgjjogkSXIdAwAAADbIZjHSDQAAAJsjpRsAAABSonQDAABASjaLe7q3FvPHeh0aAADAlsRINwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEiJ0g0AAAApUboBAAAgJTVzHSBtSZJERERJSUmOkwAAALClWN0xV3fOtdniS/eSJUsiIqKoqCjHSQAAANjSLFmyJAoLC9e6PpOsr5Zv5latWhUff/xx1K9fPzKZTK7j5FRJSUkUFRXFggULoqCgINdxwDlJteS8pLpxTlLdOCepjnJxXiZJEkuWLIlmzZrFNtus/c7tLX6ke5tttonmzZvnOka1UlBQ4F+QVCvOSaoj5yXVjXOS6sY5SXW0qc/LdY1wr+ZBagAAAJASpRsAAABSonRvRfLy8mLEiBGRl5eX6ygQEc5JqifnJdWNc5LqxjlJdVSdz8st/kFqAAAAkCtGugEAACAlSjcAAACkROkGAACAlCjdW4nx48dHq1atonbt2rH//vvHK6+8kutIbMVefPHF6Nu3bzRr1iwymUxMmTIl15HYyo0ZMyb23XffqF+/fjRu3DiOOeaYmD17dq5jsZWbMGFCdOzYMfvO2a5du8bjjz+e61iQNXbs2MhkMnH++efnOgpbqZEjR0Ymkyk3tW/fPtex1qB0bwXuv//+GDJkSIwYMSJmzJgRnTp1il69esWnn36a62hspZYtWxadOnWK8ePH5zoKRETECy+8EIMHD46XX345nn766fjmm2/iiCOOiGXLluU6Glux5s2bx9ixY+PVV1+N6dOnx6GHHhpHH310vPnmm7mOBjFt2rS46aabomPHjrmOwlauQ4cOsXDhwuz097//PdeR1uDp5VuB/fffP/bdd9+4/vrrIyJi1apVUVRUFOecc04MHTo0x+nY2mUymZg8eXIcc8wxuY4CWZ999lk0btw4XnjhhTjooINyHQeyGjZsGFdffXWcdtppuY7CVmzp0qWx9957xw033BCjR4+OvfbaK8aNG5frWGyFRo4cGVOmTImZM2fmOso6Genewn399dfx6quvRs+ePbPLttlmm+jZs2e89NJLOUwGUH0VFxdHxLcFB6qDsrKyuO+++2LZsmXRtWvXXMdhKzd48ODo06dPuf+/hFyZM2dONGvWLNq0aRP9+/ePDz74INeR1lAz1wFI1+effx5lZWXRpEmTcsubNGkS77zzTo5SAVRfq1ativPPPz+6desWe+yxR67jsJWbNWtWdO3aNVasWBH16tWLyZMnx+67757rWGzF7rvvvpgxY0ZMmzYt11Eg9t9//5g0aVLsuuuusXDhwhg1alQceOCB8cYbb0T9+vVzHS9L6QaA7xg8eHC88cYb1fKeMLY+u+66a8ycOTOKi4vjgQceiAEDBsQLL7ygeJMTCxYsiPPOOy+efvrpqF27dq7jQPTu3Tv7zx07doz9998/WrZsGX/605+q1W04SvcWbocddogaNWrEJ598Um75J598Ek2bNs1RKoDq6eyzz45HH300XnzxxWjevHmu40DUqlUrdt5554iI6NKlS0ybNi2uvfbauOmmm3KcjK3Rq6++Gp9++mnsvffe2WVlZWXx4osvxvXXXx+lpaVRo0aNHCZka9egQYPYZZddYu7cubmOUo57urdwtWrVii5dusTUqVOzy1atWhVTp051TxjA/y9Jkjj77LNj8uTJ8eyzz0br1q1zHQkqtGrVqigtLc11DLZShx12WMyaNStmzpyZnfbZZ5/o379/zJw5U+Em55YuXRrvvfde7LjjjrmOUo6R7q3AkCFDYsCAAbHPPvvEfvvtF+PGjYtly5bFoEGDch2NrdTSpUvL/Q3kvHnzYubMmdGwYcNo0aJFDpOxtRo8eHDcc8898fDDD0f9+vVj0aJFERFRWFgYderUyXE6tlbDhg2L3r17R4sWLWLJkiVxzz33xPPPPx9PPvlkrqOxlapfv/4az7rIz8+P7bff3jMwyImLLroo+vbtGy1btoyPP/44RowYETVq1Ih+/frlOlo5SvdW4IQTTojPPvsshg8fHosWLYq99tornnjiiTUergabyvTp0+OQQw7Jzg8ZMiQiIgYMGBCTJk3KUSq2ZhMmTIiIiB49epRbPnHixBg4cOCmDwQR8emnn8Ypp5wSCxcujMLCwujYsWM8+eSTcfjhh+c6GkC18OGHH0a/fv3iiy++iEaNGkX37t3j5ZdfjkaNGuU6Wjne0w0AAAApcU83AAAApETpBgAAgJQo3QAAAJASpRsAAABSonQDAABASpRuAAAASInSDQAAAClRugEAACAlSjcAbCUWLVoUhx9+eOTn50eDBg3WuiyTycSUKVMq9Z0jR46MvfbaK5W8ALAlULoBoBpYtGhRnHPOOdGmTZvIy8uLoqKi6Nu3b0ydOrXK9nHNNdfEwoULY+bMmfHuu++uddnChQujd+/elfrOiy66qEozRkRMmjQp+xcAALC5q5nrAACwtZs/f35069YtGjRoEFdffXXsueee8c0338STTz4ZgwcPjnfeeadK9vPee+9Fly5dol27dutc1rRp00p/Z7169aJevXpVkg8AtkRGugEgx84666zIZDLxyiuvxLHHHhu77LJLdOjQIYYMGRIvv/xyRER88MEHcfTRR0e9evWioKAgjj/++Pjkk0/Kfc/DDz8ce++9d9SuXTvatGkTo0aNipUrV0ZERKtWreLBBx+MO+64IzKZTAwcOLDCZRFrXl7+4YcfRr9+/aJhw4aRn58f++yzT/zrX/+KiIovL7/11ltjt912i9q1a0f79u3jhhtuyK6bP39+ZDKZeOihh+KQQw6JunXrRqdOneKll16KiIjnn38+Bg0aFMXFxZHJZCKTycTIkSOr8GgDwKZlpBsAcujLL7+MJ554Iq688srIz89fY32DBg1i1apV2cL9wgsvxMqVK2Pw4MFxwgknxPPPPx8REX/729/ilFNOieuuuy4OPPDAeO+99+IXv/hFRESMGDEipk2bFqecckoUFBTEtddeG3Xq1Imvv/56jWXft3Tp0jj44INjp512ikceeSSaNm0aM2bMiFWrVlX489x9990xfPjwuP7666Nz587x2muvxRlnnBH5+fkxYMCA7HaXXXZZ/O53v4t27drFZZddFv369Yu5c+fGAQccEOPGjYvhw4fH7NmzIyKMpAOwWVO6ASCH5s6dG0mSRPv27de6zdSpU2PWrFkxb968KCoqioiIO+64Izp06BDTpk2LfffdN0aNGhVDhw7NFts2bdrEFVdcEZdcckmMGDEiGjVqFHl5eVGnTp1yl49XtOy77rnnnvjss89i2rRp0bBhw4iI2HnnndeadcSIEfH73/8+fvrTn0ZEROvWreOtt96Km266qVzpvuiii6JPnz4RETFq1Kjo0KFDzJ07N9q3bx+FhYWRyWQ26DJ3AKiulG4AyKEkSda7zdtvvx1FRUXZwh0Rsfvuu0eDBg3i7bffjn333Tdef/31+Mc//hFXXnlldpuysrJYsWJFLF++POrWrbtR+WbOnBmdO3fOFu51WbZsWbz33ntx2mmnxRlnnJFdvnLlyigsLCy3bceOHbP/vOOOO0ZExKeffrrOv3wAgM2R0g0AOdSuXbvIZDI/+GFpS5cujVGjRmVHmL+rdu3aG/29FV1yvq4MERG33HJL7L///uXW1ahRo9z8tttum/3nTCYTEbHWS9YBYHOmdANADjVs2DB69eoV48ePj3PPPXeN+7oXL14cu+22WyxYsCAWLFiQHe1+6623YvHixbH77rtHRMTee+8ds2fPXuel3xujY8eOceutt8aXX3653tHuJk2aRLNmzeLf//539O/ff6P3WatWrSgrK9vozwNAdeLp5QCQY+PHj4+ysrLYb7/94sEHH4w5c+bE22+/Hdddd1107do1evbsGXvuuWf0798/ZsyYEa+88kqccsopcfDBB8c+++wTERHDhw+PO+64I0aNGhVvvvlmvP3223HffffFf//3f/+gbP369YumTZvGMcccE//4xz/i3//+dzz44IPZp41/36hRo2LMmDFx3XXXxbvvvhuzZs2KiRMnxh/+8IdK77NVq1axdOnSmDp1anz++eexfPnyH/QzAEAuKd0AkGNt2rSJGTNmxCGHHBIXXnhh7LHHHnH44YfH1KlTY8KECZHJZOLhhx+O7bbbLg466KDo2bNntGnTJu6///7sd/Tq1SseffTReOqpp2LfffeNH/3oR3HNNddEy5Ytf1C2WrVqxVNPPRWNGzeOI488Mvbcc88YO3bsGpeLr3b66afHrbfeGhMnTow999wzDj744Jg0aVK0bt260vs84IAD4swzz4wTTjghGjVqFFddddUP+hkAIJcySWWe4AIAAABsMCPdAAAAkBKlGwAAAFKidAMAAEBKlG4AAABIidINAAAAKVG6AQAAICVKNwAAAKRE6QYAAICUKN0AAACQEqUbAAAAUqJ0AwAAQEqUbgAAAEjJ/wf2ZwGF8Q/h9gAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Dataset Columns:\")\n",
        "for col in df.columns:\n",
        "    print(col)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "96Z7EpWjmy13",
        "outputId": "65501645-079a-48d4-ddd6-126358e1a7de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dataset Columns:\n",
            "Order_ID\n",
            "Product_ID\n",
            "User_ID\n",
            "Order_Date\n",
            "Product_Category\n",
            "Product_Price\n",
            "Order_Quantity\n",
            "Discount_Applied\n",
            "Shipping_Method\n",
            "Payment_Method\n",
            "User_Age\n",
            "User_Gender\n",
            "User_Location\n",
            "Return_Status\n",
            "Return_Reason\n",
            "Days_to_Return\n",
            "Order_Value\n",
            "Return_Cost\n",
            "Profit_Loss\n",
            "CO2_Emissions\n",
            "Packaging_Waste\n",
            "CO2_Saved\n",
            "Waste_Avoided\n",
            "Age_Group\n",
            "Order_Value_Group\n",
            "Price_Group\n",
            "Return_Flag\n",
            "Order_Year\n",
            "Order_Month\n",
            "High_Discount\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Rows:\", df.shape[0])\n",
        "print(\"Columns:\", df.shape[1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8upOswlNoQt4",
        "outputId": "16a705d7-8857-4c35-e106-2c07f6f4cd16"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Rows: 5000\n",
            "Columns: 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a copy of the test data\n",
        "risk_df = X_test.copy()\n",
        "\n",
        "# Add actual and predicted results\n",
        "risk_df['Actual_Return'] = y_test.values\n",
        "risk_df['Predicted_Return'] = y_pred\n",
        "risk_df['Return_Probability'] = y_pred_probability\n",
        "\n",
        "# Add Product ID and Category using the original dataframe index\n",
        "risk_df['Product_ID'] = df.loc[X_test.index, 'Product_ID'].values\n",
        "risk_df['Product_Category'] = df.loc[X_test.index, 'Product_Category'].values\n",
        "\n",
        "# Create risk level\n",
        "risk_df['Risk_Level'] = pd.cut(\n",
        "    risk_df['Return_Probability'],\n",
        "    bins=[-0.01, 0.39, 0.69, 1.00],\n",
        "    labels=['Low', 'Medium', 'High']\n",
        ")\n",
        "\n",
        "risk_df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 226
        },
        "id": "qFJina-XoTpq",
        "outputId": "c93d0604-cd08-4e62-f381-1106b2302276"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Product_Price  Order_Quantity  Discount_Applied  User_Age  \\\n",
              "4893         607.10               2             10.89        43   \n",
              "2217        1068.75               1             15.19        56   \n",
              "3791        1366.22               3              4.49        42   \n",
              "2530         779.93               3             49.39        58   \n",
              "4020         666.94               3             47.83        29   \n",
              "\n",
              "      Days_to_Return  Order_Value  Return_Cost  Profit_Loss  CO2_Emissions  \\\n",
              "4893              51  1081.973620          200   881.973620            2.0   \n",
              "2217               0   906.406875            0   906.406875            2.0   \n",
              "3791              58  3914.630166          200  3714.630166            1.5   \n",
              "2530               0  1184.167719            0  1184.167719            1.5   \n",
              "4020               0  1043.827794            0  1043.827794            1.5   \n",
              "\n",
              "      Packaging_Waste  Order_Year  Order_Month  High_Discount  Actual_Return  \\\n",
              "4893              0.4        2023           10              1              1   \n",
              "2217              0.2        2023            1              1              0   \n",
              "3791              0.6        2023            5              1              1   \n",
              "2530              0.6        2025            8              1              0   \n",
              "4020              0.6        2023            1              1              0   \n",
              "\n",
              "      Predicted_Return  Return_Probability Product_ID Product_Category  \\\n",
              "4893                 1            0.999960   PROD0458         Clothing   \n",
              "2217                 0            0.000830   PROD0413      Electronics   \n",
              "3791                 1            0.999983   PROD0453         Clothing   \n",
              "2530                 0            0.000934   PROD0382            Books   \n",
              "4020                 0            0.000940   PROD0106  Home Appliances   \n",
              "\n",
              "     Risk_Level  \n",
              "4893       High  \n",
              "2217        Low  \n",
              "3791       High  \n",
              "2530        Low  \n",
              "4020        Low  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-11cd608a-f85b-484c-9176-425be993f4df\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Product_Price</th>\n",
              "      <th>Order_Quantity</th>\n",
              "      <th>Discount_Applied</th>\n",
              "      <th>User_Age</th>\n",
              "      <th>Days_to_Return</th>\n",
              "      <th>Order_Value</th>\n",
              "      <th>Return_Cost</th>\n",
              "      <th>Profit_Loss</th>\n",
              "      <th>CO2_Emissions</th>\n",
              "      <th>Packaging_Waste</th>\n",
              "      <th>Order_Year</th>\n",
              "      <th>Order_Month</th>\n",
              "      <th>High_Discount</th>\n",
              "      <th>Actual_Return</th>\n",
              "      <th>Predicted_Return</th>\n",
              "      <th>Return_Probability</th>\n",
              "      <th>Product_ID</th>\n",
              "      <th>Product_Category</th>\n",
              "      <th>Risk_Level</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>4893</th>\n",
              "      <td>607.10</td>\n",
              "      <td>2</td>\n",
              "      <td>10.89</td>\n",
              "      <td>43</td>\n",
              "      <td>51</td>\n",
              "      <td>1081.973620</td>\n",
              "      <td>200</td>\n",
              "      <td>881.973620</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.4</td>\n",
              "      <td>2023</td>\n",
              "      <td>10</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999960</td>\n",
              "      <td>PROD0458</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2217</th>\n",
              "      <td>1068.75</td>\n",
              "      <td>1</td>\n",
              "      <td>15.19</td>\n",
              "      <td>56</td>\n",
              "      <td>0</td>\n",
              "      <td>906.406875</td>\n",
              "      <td>0</td>\n",
              "      <td>906.406875</td>\n",
              "      <td>2.0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>2023</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.000830</td>\n",
              "      <td>PROD0413</td>\n",
              "      <td>Electronics</td>\n",
              "      <td>Low</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3791</th>\n",
              "      <td>1366.22</td>\n",
              "      <td>3</td>\n",
              "      <td>4.49</td>\n",
              "      <td>42</td>\n",
              "      <td>58</td>\n",
              "      <td>3914.630166</td>\n",
              "      <td>200</td>\n",
              "      <td>3714.630166</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.6</td>\n",
              "      <td>2023</td>\n",
              "      <td>5</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999983</td>\n",
              "      <td>PROD0453</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2530</th>\n",
              "      <td>779.93</td>\n",
              "      <td>3</td>\n",
              "      <td>49.39</td>\n",
              "      <td>58</td>\n",
              "      <td>0</td>\n",
              "      <td>1184.167719</td>\n",
              "      <td>0</td>\n",
              "      <td>1184.167719</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.6</td>\n",
              "      <td>2025</td>\n",
              "      <td>8</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.000934</td>\n",
              "      <td>PROD0382</td>\n",
              "      <td>Books</td>\n",
              "      <td>Low</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4020</th>\n",
              "      <td>666.94</td>\n",
              "      <td>3</td>\n",
              "      <td>47.83</td>\n",
              "      <td>29</td>\n",
              "      <td>0</td>\n",
              "      <td>1043.827794</td>\n",
              "      <td>0</td>\n",
              "      <td>1043.827794</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.6</td>\n",
              "      <td>2023</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0.000940</td>\n",
              "      <td>PROD0106</td>\n",
              "      <td>Home Appliances</td>\n",
              "      <td>Low</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-11cd608a-f85b-484c-9176-425be993f4df')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-11cd608a-f85b-484c-9176-425be993f4df button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-11cd608a-f85b-484c-9176-425be993f4df');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "risk_df",
              "summary": "{\n  \"name\": \"risk_df\",\n  \"rows\": 1000,\n  \"fields\": [\n    {\n      \"column\": \"Product_Price\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 560.4622274234362,\n        \"min\": 101.62,\n        \"max\": 1993.04,\n        \"num_unique_values\": 993,\n        \"samples\": [\n          1499.2,\n          1365.49,\n          1968.84\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Quantity\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 5,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          1,\n          5,\n          3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Discount_Applied\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14.48673788146753,\n        \"min\": 0.05,\n        \"max\": 49.97,\n        \"num_unique_values\": 906,\n        \"samples\": [\n          26.51,\n          42.53,\n          29.31\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"User_Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 13,\n        \"min\": 18,\n        \"max\": 65,\n        \"num_unique_values\": 48,\n        \"samples\": [\n          65,\n          31,\n          23\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Days_to_Return\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 17,\n        \"min\": 0,\n        \"max\": 60,\n        \"num_unique_values\": 56,\n        \"samples\": [\n          51,\n          9,\n          52\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Value\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1839.7099910963955,\n        \"min\": 68.826835,\n        \"max\": 9051.19782,\n        \"num_unique_values\": 1000,\n        \"samples\": [\n          2680.52626,\n          1104.9785880000002,\n          1262.785804\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Return_Cost\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 90,\n        \"min\": 0,\n        \"max\": 200,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          200\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Profit_Loss\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1844.1964481968375,\n        \"min\": -130.665337,\n        \"max\": 9051.19782,\n        \"num_unique_values\": 1000,\n        \"samples\": [\n          2680.52626,\n          1104.9785880000002\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"CO2_Emissions\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.4138974040279336,\n        \"min\": 1.0,\n        \"max\": 2.0,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          2.0,\n          1.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Packaging_Waste\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.27906256631070453,\n        \"min\": 0.2,\n        \"max\": 1.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.2,\n          1.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Year\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2025,\n          2022\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Order_Month\",\n      \"properties\": {\n        \"dtype\": \"int32\",\n        \"num_unique_values\": 12,\n        \"samples\": [\n          12,\n          9\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"High_Discount\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Actual_Return\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Predicted_Return\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Return_Probability\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.45275441592854754,\n        \"min\": 0.000634058437526517,\n        \"max\": 0.9999896127464722,\n        \"num_unique_values\": 1000,\n        \"samples\": [\n          0.0006918850833814455,\n          0.0009547409332265285\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Product_ID\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 434,\n        \"samples\": [\n          \"PROD0490\",\n          \"PROD0500\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Product_Category\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Electronics\",\n          \"Toys\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Risk_Level\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Low\",\n          \"High\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "product_risk = (\n",
        "    risk_df.groupby(\n",
        "        ['Product_ID', 'Product_Category'],\n",
        "        as_index=False\n",
        "    )\n",
        "    .agg(\n",
        "        Orders=('Product_ID', 'count'),\n",
        "        Actual_Returns=('Actual_Return', 'sum'),\n",
        "        Average_Return_Probability=('Return_Probability', 'mean')\n",
        "    )\n",
        ")\n",
        "\n",
        "product_risk['Actual_Return_Rate'] = (\n",
        "    product_risk['Actual_Returns'] /\n",
        "    product_risk['Orders'] * 100\n",
        ")\n",
        "\n",
        "product_risk['Risk_Level'] = pd.cut(\n",
        "    product_risk['Average_Return_Probability'],\n",
        "    bins=[-0.01, 0.39, 0.69, 1.00],\n",
        "    labels=['Low', 'Medium', 'High']\n",
        ")\n",
        "\n",
        "product_risk = product_risk.sort_values(\n",
        "    'Average_Return_Probability',\n",
        "    ascending=False\n",
        ")\n",
        "\n",
        "product_risk.head(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 363
        },
        "id": "dVidbQasokWp",
        "outputId": "43281033-2f31-43a9-cf53-3b1c8e35bef6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Product_ID Product_Category  Orders  Actual_Returns  \\\n",
              "682   PROD0426      Electronics       1               1   \n",
              "101   PROD0066            Books       1               1   \n",
              "194   PROD0125      Electronics       1               1   \n",
              "307   PROD0191         Clothing       1               1   \n",
              "261   PROD0164         Clothing       1               1   \n",
              "346   PROD0214            Books       1               1   \n",
              "423   PROD0254             Toys       1               1   \n",
              "20    PROD0010  Home Appliances       1               1   \n",
              "373   PROD0228            Books       1               1   \n",
              "785   PROD0498         Clothing       1               1   \n",
              "\n",
              "     Average_Return_Probability  Actual_Return_Rate Risk_Level  \n",
              "682                    0.999990               100.0       High  \n",
              "101                    0.999987               100.0       High  \n",
              "194                    0.999987               100.0       High  \n",
              "307                    0.999987               100.0       High  \n",
              "261                    0.999986               100.0       High  \n",
              "346                    0.999986               100.0       High  \n",
              "423                    0.999985               100.0       High  \n",
              "20                     0.999984               100.0       High  \n",
              "373                    0.999983               100.0       High  \n",
              "785                    0.999983               100.0       High  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7e8bb501-9a0c-4129-9e35-93ad9018dea1\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Product_ID</th>\n",
              "      <th>Product_Category</th>\n",
              "      <th>Orders</th>\n",
              "      <th>Actual_Returns</th>\n",
              "      <th>Average_Return_Probability</th>\n",
              "      <th>Actual_Return_Rate</th>\n",
              "      <th>Risk_Level</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>682</th>\n",
              "      <td>PROD0426</td>\n",
              "      <td>Electronics</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999990</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>101</th>\n",
              "      <td>PROD0066</td>\n",
              "      <td>Books</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999987</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>194</th>\n",
              "      <td>PROD0125</td>\n",
              "      <td>Electronics</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999987</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>307</th>\n",
              "      <td>PROD0191</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999987</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>261</th>\n",
              "      <td>PROD0164</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999986</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>346</th>\n",
              "      <td>PROD0214</td>\n",
              "      <td>Books</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999986</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>423</th>\n",
              "      <td>PROD0254</td>\n",
              "      <td>Toys</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999985</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>PROD0010</td>\n",
              "      <td>Home Appliances</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999984</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>373</th>\n",
              "      <td>PROD0228</td>\n",
              "      <td>Books</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999983</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>785</th>\n",
              "      <td>PROD0498</td>\n",
              "      <td>Clothing</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0.999983</td>\n",
              "      <td>100.0</td>\n",
              "      <td>High</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7e8bb501-9a0c-4129-9e35-93ad9018dea1')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7e8bb501-9a0c-4129-9e35-93ad9018dea1 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7e8bb501-9a0c-4129-9e35-93ad9018dea1');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "product_risk",
              "summary": "{\n  \"name\": \"product_risk\",\n  \"rows\": 791,\n  \"fields\": [\n    {\n      \"column\": \"Product_ID\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 434,\n        \"samples\": [\n          \"PROD0343\",\n          \"PROD0330\",\n          \"PROD0239\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Product_Category\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Books\",\n          \"Home Appliances\",\n          \"Clothing\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Orders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 4,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          4,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Actual_Returns\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 3,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Average_Return_Probability\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.4171330856819554,\n        \"min\": 0.000634058437526517,\n        \"max\": 0.9999896127464722,\n        \"num_unique_values\": 791,\n        \"samples\": [\n          0.49404821051983466,\n          0.9999416587207867,\n          0.000880228057887441\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Actual_Return_Rate\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 41.82492469240946,\n        \"min\": 0.0,\n        \"max\": 100.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          100.0,\n          66.66666666666666,\n          0.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Risk_Level\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"High\",\n          \"Medium\",\n          \"Low\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "high_risk_products = product_risk[\n",
        "    product_risk['Risk_Level'] == 'High'\n",
        "].copy()\n",
        "\n",
        "high_risk_products.to_csv(\n",
        "    '/content/high_risk_products.csv',\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"High-risk products:\", len(high_risk_products))\n",
        "print(\"CSV created successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2gTHte0Pond2",
        "outputId": "50801c81-e701-4c55-db95-66ab1a45056d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "High-risk products: 178\n",
            "CSV created successfully.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Predict probability for the complete dataset\n",
        "X_all_scaled = scaler.transform(X)\n",
        "\n",
        "df['Predicted_Return_Probability'] = model.predict_proba(X_all_scaled)[:, 1]\n",
        "\n",
        "# Create risk levels\n",
        "df['Risk_Level'] = pd.cut(\n",
        "    df['Predicted_Return_Probability'],\n",
        "    bins=[-0.01, 0.39, 0.69, 1.00],\n",
        "    labels=['Low', 'Medium', 'High']\n",
        ")\n",
        "\n",
        "print(df[['Product_ID',\n",
        "          'Predicted_Return_Probability',\n",
        "          'Risk_Level']].head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mf1FuHdoopxy",
        "outputId": "a83be7c6-b348-44a8-d4f8-5432312fa880"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Product_ID  Predicted_Return_Probability Risk_Level\n",
            "0   PROD0169                      0.000881        Low\n",
            "1   PROD0318                      0.995055       High\n",
            "2   PROD0427                      0.000945        Low\n",
            "3   PROD0323                      0.000722        Low\n",
            "4   PROD0325                      0.994576       High\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df['Risk_Level'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WV3Z_rPno7Y2",
        "outputId": "bd437dbc-26c4-4390-ee91-7afc0ab07cf8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Risk_Level\n",
            "Low       3550\n",
            "High      1450\n",
            "Medium       0\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "powerbi_df = df.copy()\n",
        "\n",
        "powerbi_df.to_csv(\n",
        "    '/content/ecommerce_return_powerbi.csv',\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"Power BI dataset created successfully.\")\n",
        "print(\"Rows:\", powerbi_df.shape[0])\n",
        "print(\"Columns:\", powerbi_df.shape[1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fMTuA1NBo9o3",
        "outputId": "df082b08-ebe0-47f2-d0ee-d397c88b9554"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Power BI dataset created successfully.\n",
            "Rows: 5000\n",
            "Columns: 32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create meaningful risk groups based on predicted probability\n",
        "df['Risk_Level'] = pd.qcut(\n",
        "    df['Predicted_Return_Probability'],\n",
        "    q=[0, 0.50, 0.80, 1.00],\n",
        "    labels=['Low', 'Medium', 'High'],\n",
        "    duplicates='drop'\n",
        ")\n",
        "\n",
        "print(df['Risk_Level'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NilJ-BvqpANr",
        "outputId": "a2945e10-e299-4a66-9a63-6acfcdaf0441"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Risk_Level\n",
            "Low       2500\n",
            "Medium    1500\n",
            "High      1000\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "risk_summary = (\n",
        "    df.groupby('Risk_Level', observed=True)['Predicted_Return_Probability']\n",
        "      .agg(['count', 'min', 'max', 'mean'])\n",
        ")\n",
        "\n",
        "print(risk_summary)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6VM8dJhnpO4P",
        "outputId": "213cc07d-7147-4084-d56b-02965fcef214"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            count       min       max      mean\n",
            "Risk_Level                                     \n",
            "Low          2500  0.000600  0.000858  0.000776\n",
            "Medium       1500  0.000858  0.998541  0.299014\n",
            "High         1000  0.998551  0.999990  0.999674\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "powerbi_df = df.copy()\n",
        "\n",
        "powerbi_df.to_csv(\n",
        "    '/content/ecommerce_return_powerbi.csv',\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"Power BI dataset created successfully.\")\n",
        "print(\"Rows:\", powerbi_df.shape[0])\n",
        "print(\"Columns:\", powerbi_df.shape[1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CrZj6C6BpRu6",
        "outputId": "28adc301-2a99-428a-db4b-ba4a27981c82"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Power BI dataset created successfully.\n",
            "Rows: 5000\n",
            "Columns: 32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "risk_summary = (\n",
        "    df.groupby('Risk_Level', observed=True)['Predicted_Return_Probability']\n",
        "      .agg(['count', 'min', 'max', 'mean'])\n",
        ")\n",
        "\n",
        "print(risk_summary)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WiZaco5_pT22",
        "outputId": "868b03b4-7541-4e99-fa3a-9f41a58cb6b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            count       min       max      mean\n",
            "Risk_Level                                     \n",
            "Low          2500  0.000600  0.000858  0.000776\n",
            "Medium       1500  0.000858  0.998541  0.299014\n",
            "High         1000  0.998551  0.999990  0.999674\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "powerbi_df = df.copy()\n",
        "\n",
        "powerbi_df.to_csv(\n",
        "    '/content/ecommerce_return_powerbi.csv',\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"Power BI dataset created successfully.\")\n",
        "print(\"Rows:\", powerbi_df.shape[0])\n",
        "print(\"Columns:\", powerbi_df.shape[1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v7lP1mkjpkpj",
        "outputId": "11728cf7-0a36-460b-f0d6-7f3ac790559c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Power BI dataset created successfully.\n",
            "Rows: 5000\n",
            "Columns: 32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(powerbi_df[['Product_ID',\n",
        "                  'Product_Category',\n",
        "                  'Predicted_Return_Probability',\n",
        "                  'Risk_Level']].head(10))"
      ],
      "metadata": {
        "id": "CPv7rNyOptXt",
        "outputId": "c4bf3c29-0523-4185-df48-92785c6392c4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Product_ID Product_Category  Predicted_Return_Probability Risk_Level\n",
            "0   PROD0169         Clothing                      0.000881     Medium\n",
            "1   PROD0318             Toys                      0.995055     Medium\n",
            "2   PROD0427         Clothing                      0.000945     Medium\n",
            "3   PROD0323            Books                      0.000722        Low\n",
            "4   PROD0325  Home Appliances                      0.994576     Medium\n",
            "5   PROD0490  Home Appliances                      0.000881     Medium\n",
            "6   PROD0203         Clothing                      0.999950       High\n",
            "7   PROD0309  Home Appliances                      0.000794        Low\n",
            "8   PROD0477            Books                      0.000889     Medium\n",
            "9   PROD0013         Clothing                      0.999873       High\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "features = [\n",
        "    'Product_Price',\n",
        "    'Order_Quantity',\n",
        "    'Discount_Applied',\n",
        "    'User_Age',\n",
        "    'Order_Value',\n",
        "    'Order_Year',\n",
        "    'Order_Month'\n",
        "]"
      ],
      "metadata": {
        "id": "4zRsIUfrpvN2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df[features]\n",
        "y = df['Return_Flag']"
      ],
      "metadata": {
        "id": "ZSF__fgkyPVv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Features:\")\n",
        "print(X.columns.tolist())\n",
        "\n",
        "print(\"\\nX shape:\", X.shape)\n",
        "print(\"y shape:\", y.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zDLdrhdNynaT",
        "outputId": "a8faf55f-34b1-4001-8a71-9b428988bb52"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Features:\n",
            "['Product_Price', 'Order_Quantity', 'Discount_Applied', 'User_Age', 'Order_Value', 'Order_Year', 'Order_Month']\n",
            "\n",
            "X shape: (5000, 7)\n",
            "y shape: (5000,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size=0.20,\n",
        "    random_state=42,\n",
        "    stratify=y\n",
        ")\n",
        "\n",
        "print(\"Training data:\", X_train.shape)\n",
        "print(\"Testing data:\", X_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vyhWFqq_yvZC",
        "outputId": "abc3c929-0dd6-43cf-9183-c5815429b90a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training data: (4000, 7)\n",
            "Testing data: (1000, 7)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "scaler = StandardScaler()\n",
        "\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)\n",
        "\n",
        "print(\"Training scaled shape:\", X_train_scaled.shape)\n",
        "print(\"Testing scaled shape:\", X_test_scaled.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nXKEo_L0y1kg",
        "outputId": "a8ba5a2a-c85d-4dbb-bbb3-09624b9e80ba"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training scaled shape: (4000, 7)\n",
            "Testing scaled shape: (1000, 7)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "model = LogisticRegression(random_state=42)\n",
        "\n",
        "model.fit(X_train_scaled, y_train)\n",
        "\n",
        "print(\"Logistic Regression model trained successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iue3GlNsy7C2",
        "outputId": "5d223e7a-8322-4dd7-da37-a1ffad6b549b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Logistic Regression model trained successfully.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test_scaled)\n",
        "\n",
        "y_pred_probability = model.predict_proba(X_test_scaled)[:, 1]\n",
        "\n",
        "print(\"Predictions generated successfully.\")\n",
        "print(\"Number of predictions:\", len(y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RKQvvkLVzBAg",
        "outputId": "ac60b55c-8740-425b-ee4e-5d374db2cab6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predictions generated successfully.\n",
            "Number of predictions: 1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score, precision_score, recall_score\n",
        "\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "precision = precision_score(y_test, y_pred)\n",
        "recall = recall_score(y_test, y_pred)\n",
        "\n",
        "print(\"Accuracy:\", round(accuracy, 4))\n",
        "print(\"Precision:\", round(precision, 4))\n",
        "print(\"Recall:\", round(recall, 4))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a1rVATCTzGGc",
        "outputId": "8049cedb-6872-498e-899b-e4f9d248fe88"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.71\n",
            "Precision: 0.0\n",
            "Recall: 0.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.13/dist-packages/sklearn/metrics/_classification.py:1565: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 due to no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, f\"{metric.capitalize()} is\", len(result))\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Actual classes:\")\n",
        "print(y_test.value_counts())\n",
        "\n",
        "print(\"\\nPredicted classes:\")\n",
        "print(pd.Series(y_pred).value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m2L9043lzMUn",
        "outputId": "3609c0f7-45eb-4468-9beb-258ee81b7113"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Actual classes:\n",
            "Return_Flag\n",
            "0    710\n",
            "1    290\n",
            "Name: count, dtype: int64\n",
            "\n",
            "Predicted classes:\n",
            "0    1000\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "\n",
        "model = LogisticRegression(\n",
        "    random_state=42,\n",
        "    class_weight='balanced'\n",
        ")\n",
        "\n",
        "model.fit(X_train_scaled, y_train)\n",
        "\n",
        "print(\"Balanced Logistic Regression model trained successfully.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SSB4omKOzVeq",
        "outputId": "7fd0dea2-753a-409d-9d91-7359f415ef31"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Balanced Logistic Regression model trained successfully.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test_scaled)\n",
        "y_pred_probability = model.predict_proba(X_test_scaled)[:, 1]\n",
        "\n",
        "print(\"Predicted classes:\")\n",
        "print(pd.Series(y_pred).value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uwO7JFZLzjw0",
        "outputId": "6813c11a-098c-423c-da2b-6509f8298e80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted classes:\n",
            "0    506\n",
            "1    494\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\n",
        "\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "precision = precision_score(y_test, y_pred)\n",
        "recall = recall_score(y_test, y_pred)\n",
        "f1 = f1_score(y_test, y_pred)\n",
        "\n",
        "print(\"Accuracy:\", round(accuracy, 4))\n",
        "print(\"Precision:\", round(precision, 4))\n",
        "print(\"Recall:\", round(recall, 4))\n",
        "print(\"F1 Score:\", round(f1, 4))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_m-vyp36zz8g",
        "outputId": "f035d850-0f8a-4964-8616-74bc51b41aca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 0.52\n",
            "Precision: 0.3077\n",
            "Recall: 0.5241\n",
            "F1 Score: 0.3878\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "cm = confusion_matrix(y_test, y_pred)\n",
        "\n",
        "print(\"Confusion Matrix:\")\n",
        "print(cm)\n",
        "\n",
        "disp = ConfusionMatrixDisplay(\n",
        "    confusion_matrix=cm,\n",
        "    display_labels=['Not Returned', 'Returned']\n",
        ")\n",
        "\n",
        "disp.plot()\n",
        "plt.title(\"Logistic Regression Confusion Matrix\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 524
        },
        "id": "KKOeupVBz6ED",
        "outputId": "8d2c2e30-f151-4cb5-e172-33fc3457bd70"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Confusion Matrix:\n",
            "[[368 342]\n",
            " [138 152]]\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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+uorfPXVV3mWcXNzw549e/SOhYkTERERyaKGBDX0GKrTo25xY+JEREREsvAlv0RERESUL/Y4ERERkSxFPTm8JGHiRERERLKU5aE6Jk5EREQkS1nuceIcJyIiIiIdsceJiIiIZBF6DtWV5h4nJk5EREQkiwAghH71SysO1RERERHpiD1OREREJIsaEiSuHE5ERESUPz5VR0RERET5Yo8TERERyaIWEiQugElERESUPyH0fKquFD9Wx6E6IiIiIh2xx4mIiIhkKcuTw5k4ERERkSxMnIiIiIh0VJYnh3OOExEREZGO2ONEREREspTlp+qYOBEREZEszxMnfeY4FWAwRYxDdUREREQ6Yo8TERERycKn6oiIiIh0JP636VO/tOJQHREREZGO2ONEREREsnCojoiIiEhXZXisjokTERERyaNnjxNKcY8T5zgRERER6Yg9TkRERCQLVw4nIiIi0lFZnhzOoToiIiIiHbHHiYiIiOQRkn4TvEtxjxMTJyIiIpKlLM9x4lAdERERkY7Y40RERETycAHMV/v55591PuG777772sEQERFRyVeWn6rTKXHq3LmzTieTJAkqlUqfeIiIiIhKLJ0SJ7VaXdhxEBERUWlSiofb9KHXHKe0tDSYmpoWVCxERERUCpTloTrZT9WpVCrMnj0bFStWhKWlJa5duwYAmDZtGtasWVPgARIREVEJIwpgK6VkJ05z5sxBWFgYFixYABMTE83+mjVrYvXq1QUaHBEREVFJIjtx2rBhA7755hv06dMHhoaGmv21a9fGpUuXCjQ4IiIiKomkAthKJ9lznO7cuQNPT88c+9VqNTIzMwskKCIiIirByvA6TrJ7nHx8fPD777/n2L9t2zbUqVOnQIIiIiIiKolk9zhNnz4dQUFBuHPnDtRqNXbs2IHo6Ghs2LAB4eHhhREjERERlSTscdJdp06dsHv3bhw8eBAWFhaYPn06oqKisHv3brRp06YwYiQiIqKSREj6b6XUa63j1KRJE0RERBR0LEREREQl2msvgHn69GlERUUBeD7vqV69egUWFBEREZVcQjzf9KlfWslOnG7fvo1evXrh+PHjsLGxAQAkJSXh//7v//DDDz/AxcWloGMkIiKikoRznHQ3ePBgZGZmIioqComJiUhMTERUVBTUajUGDx5cGDESERERlQiye5yOHj2KEydOwMvLS7PP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RyCDtbW11mcDAwN4eXlh1qxZCAgIKLDAiIiIiEoaWYmTSqXCgAED4Ovri3LlyhVWTEREREQlkqzJ4YaGhggICEBSUlIhhUNEREQlXhl+V53sp+pq1qyJa9euFUYsREREVApkz3HSZyutZCdOn332GSZMmIDw8HDExcUhJSVFayMiIiJ6U+k8x2nWrFkYP3482rdvDwB49913tV69IoSAJElQqVQFHyURERGVLKW410gfOidOM2fOxNChQ3H48OHCjIeIiIhKOq7jlD8hnl9ls2bNCi0YIiIiopJM1nIELw7NERERUdnEBTB1VK1atXyTp8TERL0CIiIiohKOQ3W6mTlzZo6Vw4mIiIjKClmJU8+ePWFvb19YsRAREVEpwKE6HXB+ExEREQEo00N1Oi+Amf1UHREREVFZpXOPk1qtLsw4iIiIqLQowz1OsuY4EREREXGOExEREZGuynCPk+yX/BIRERGVVexxIiIiInnKcI8TEyciIiKSpSzPceJQHREREZGO2ONERERE8nCojoiIiEg3HKojIiIionyxx4mIiIjk4VAdERERkY7KcOLEoToiIiIiHbHHiYiIiGSR/rfpU7+0YuJERERE8pThoTomTkRERCQLlyMgIiIionyxx4mIiIjk4VAdERERkQylOPnRB4fqiIiIiHTEHiciIiKSpSxPDmfiRERERPKU4TlOHKojIiIi0hF7nIiIiEgWDtURERER6YpDdURERESUH/Y4ERERkSwcqiMiIiLSVRkeqmPiRERERPKU4cSJc5yIiIiIdMQeJyIiIpKFc5yIiIiIdMWhOiIiIiLKD3uciIiISBZJCEji9buN9Klb3Jg4ERERkTwcqiMiIiKi/LDHiYiIiGThU3VEREREuuJQHRERERHlhz1OREREJAuH6oiIiIh0VYaH6pg4ERERkSxluceJc5yIiIiIdMQeJyIiIpKHQ3VEREREuivNw2364FAdERERkY6YOBEREZE8Qui/yRAaGoq33noLVlZWsLe3R+fOnREdHa1VJi0tDcOHD0f58uVhaWmJrl274t69e1plbt68iQ4dOsDc3Bz29vaYOHEisrKyZMXCxImIiIhkyX6qTp9NjqNHj2L48OE4deoUIiIikJmZiYCAADx58kRTZuzYsdi9eze2bt2Ko0eP4u7du+jSpYvmuEqlQocOHZCRkYETJ05g/fr1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Z4fQ0FBcu3YNNjY2qFu3Lj7++GMAQMWKFTFz5kxMmTIFAwYMQP/+/REWFoapU6fi+vXreOedd2BtbY3Zs2cXSI8TAMyePfuVMVWqVAnbt2/H2LFjsWzZMrz99tuYO3cuBg4cWCDtk+7+OWmJQOfaeR6fPdg933Nc+cccn/T2KMCoiArO+dO2r0xwpn1U95X1D/7sjIM/Oxd0WFTEyvJQnSR0ecaP3ngpKSmwtrZGc3SCkcQnt+jNZGhnV9whEBWaLHUGDj1Yg+TkZFmvMZEj+3eFf9tZMDI2fe3zZGWm4eS+6YUaa2EpkwtgEhEREb0ODtURERGRLGV5qI6JExEREcmjFs83feqXUkyciIiISJ4yvHI45zgRERER6Yg9TkRERCSLBD3nOBVYJEWPiRMRERHJU4ZXDudQHREREZGO2ONEREREsnA5AiIiIiJd8ak6IiIiIsoPe5yIiIhIFkkISHpM8NanbnFj4kRERETyqP+36VO/lOJQHREREZGO2ONEREREsnCojoiIiEhXZfipOiZOREREJA9XDiciIiKi/LDHiYiIiGThyuFEREREuuJQHRERERHlhz1OREREJIukfr7pU7+0YuJERERE8nCojoiIiIjywx4nIiIikocLYBIRERHppiy/coVDdUREREQ6Yo8TERERyVOGJ4czcSIiIiJ5BAB9lhQovXkTEyciIiKSh3OciIiIiChf7HEiIiIieQT0nONUYJEUOSZOREREJE8ZnhzOoToiIiIiHbHHiYiIiORRA5D0rF9KMXEiIiIiWfhUHRERERHliz1OREREJE8ZnhzOxImIiIjkKcOJE4fqiIiIiHTEHiciIiKSpwz3ODFxIiIiInm4HAERERGRbrgcARERERHliz1OREREJA/nOBERERHpSC0ASY/kR116EycO1RERERHpiD1OREREJA+H6oiIiIh0pWfihNKbOHGojoiIiEhH7HEiIiIieThUR0RERKQjtYBew218qo6IiIjozcceJyIiIpJHqJ9v+tQvpZg4ERERkTyc40RERESkI85xIiIiIqL8sMeJiIiI5OFQHREREZGOBPRMnAoskiLHoToiIiIiHbHHiYiIiOThUB0RERGRjtRqAHqsxaQuves4caiOiIiISrzffvsNHTt2hLOzMyRJwq5du7SOBwcHQ5Ikra1t27ZaZRITE9GnTx8olUrY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CZydnWFkpP2/DgsLC63PqampqFevHjZt2pTjXHZ2dq8Vg5mZmew6qampAIBffvlFK2EBns/bKignT55Enz59MHPmTAQGBsLa2ho//PADFi1aJDvWb7/9NkciZ2hoWGCxEpF+mDgRUb4sLCzg6empc/m6detiy5YtsLe3z9Hrks3JyQl//PEHmjZtCuB5z8qZM2dQt27dXMv7+vpCrVbj6NGjaN26dY7j2T1eKpVKs8/HxwcKhQI3b97Ms6fK29tbM9E926lTp/K/yBecOHECbm5u+OSTTzT7bty4kaPczZs3cffuXTg7O2vaMTAwgJeXFxwcHODs7Ixr166hT58+stonoqLDyeFEVOD69OmDChUqoFOnTvj9999x/fp1HDlyBKNGjcLt27cBAKNHj8a8efOwa9cuXLp0CcOGDXvlGkzu7u4ICgrCwIEDsWvXLs05f/zxRwCAm5sbJElCeHg47t+/j9TUVFhZWWHChAkYO3Ys1q9fj5iYGPz9999YtmyZZsL10KFDceXKFUycOBHR0dHYvHkzwsLCZF1v1apVcfPmTfzwww+IiYnB0qVLc53obmpqiqCgIJw7dw6///47Ro0ahe7du8PR0REAMHPmTISGhmLp0qW4fPkyzp8/j3Xr1uGLL76QFQ8RFR4mTkRU4MzNzfHbb7+hUqVK6NKlC7y9vTFo0CCkpaVpeqDGjx+Pfv36ISgoCP7+/rCyssJ77733yvOuWLEC77//PoYNG4bq1atjyJAhePLkCQCgYsWKmDlzJqZMmQIHBweMGDECADB79mxMmzYNoaGh8Pb2Rtu2bfHLL7+gcuXKAJ7PO9q+fTt27dqF2rVrY+XKlZg7d66s63333XcxduxYjBgxAn5+fjhx4gSmTZuWo5ynpye6dOmC9u3bIyAgALVq1dJabmDw4MFYvXo11q1bB19fXzRr1gxhYWGaWImo+Ekir5mYRERERKSFPU5EREREOmLiRERERKQjJk5EREREOmLiRERERKQjJk5EREREOmLiRERERKQjJk5EREREOmLiRERERKQjJk5EREREOmLiRERERKQjJk5EREREOmLiRERERKSj/wfmfo5R6LDJcgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "coefficients = pd.DataFrame({\n",
        "    'Feature': features,\n",
        "    'Coefficient': model.coef_[0]\n",
        "})\n",
        "\n",
        "coefficients['Absolute_Coefficient'] = coefficients['Coefficient'].abs()\n",
        "\n",
        "coefficients = coefficients.sort_values(\n",
        "    by='Absolute_Coefficient',\n",
        "    ascending=False\n",
        ")\n",
        "\n",
        "print(coefficients)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cI_aCtaT0AzJ",
        "outputId": "81ee2ad6-159d-4b39-f447-9ed9f1cccf7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            Feature  Coefficient  Absolute_Coefficient\n",
            "2  Discount_Applied     0.192945              0.192945\n",
            "4       Order_Value     0.069087              0.069087\n",
            "1    Order_Quantity    -0.062646              0.062646\n",
            "5        Order_Year     0.054597              0.054597\n",
            "6       Order_Month     0.024326              0.024326\n",
            "0     Product_Price    -0.017528              0.017528\n",
            "3          User_Age     0.015065              0.015065\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_all_scaled = scaler.transform(X)\n",
        "\n",
        "df['Predicted_Return_Probability'] = model.predict_proba(\n",
        "    X_all_scaled\n",
        ")[:, 1]\n",
        "\n",
        "print(df['Predicted_Return_Probability'].describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6Z4D3Zv_0Hwc",
        "outputId": "c6556227-c0aa-43b0-b4ce-6c0f49f4597a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "count    5000.000000\n",
            "mean        0.498094\n",
            "std         0.047362\n",
            "min         0.373946\n",
            "25%         0.460074\n",
            "50%         0.498843\n",
            "75%         0.535868\n",
            "max         0.608013\n",
            "Name: Predicted_Return_Probability, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Risk_Level'] = pd.qcut(\n",
        "    df['Predicted_Return_Probability'],\n",
        "    q=[0, 0.50, 0.80, 1.00],\n",
        "    labels=['Low', 'Medium', 'High'],\n",
        "    duplicates='drop'\n",
        ")\n",
        "\n",
        "print(df['Risk_Level'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5JhUxFkG0PCD",
        "outputId": "2fc77854-467d-47c1-8286-a3b5188896ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Risk_Level\n",
            "Low       2500\n",
            "Medium    1500\n",
            "High      1000\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\n",
        "    df.groupby('Risk_Level')['Predicted_Return_Probability']\n",
        "      .agg(['count', 'min', 'max', 'mean'])\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SCbKqkeG0W8j",
        "outputId": "521d7a06-9270-48ba-f091-8336d208a4d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            count       min       max      mean\n",
            "Risk_Level                                     \n",
            "Low          2500  0.373946  0.498831  0.458040\n",
            "Medium       1500  0.498854  0.543865  0.521001\n",
            "High         1000  0.543868  0.608013  0.563872\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_6542/1903565035.py:2: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.\n",
            "  df.groupby('Risk_Level')['Predicted_Return_Probability']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "product_risk = (\n",
        "    df.groupby(\n",
        "        ['Product_ID', 'Product_Category'],\n",
        "        as_index=False\n",
        "    )\n",
        "    .agg(\n",
        "        Orders=('Product_ID', 'count'),\n",
        "        Actual_Returns=('Return_Flag', 'sum'),\n",
        "        Average_Return_Probability=('Predicted_Return_Probability', 'mean')\n",
        "    )\n",
        ")\n",
        "\n",
        "product_risk['Actual_Return_Rate'] = (\n",
        "    product_risk['Actual_Returns'] /\n",
        "    product_risk['Orders'] * 100\n",
        ")\n",
        "\n",
        "product_risk['Risk_Level'] = pd.cut(\n",
        "    product_risk['Average_Return_Probability'],\n",
        "    bins=[\n",
        "        -float('inf'),\n",
        "        df['Predicted_Return_Probability'].quantile(0.50),\n",
        "        df['Predicted_Return_Probability'].quantile(0.80),\n",
        "        float('inf')\n",
        "    ],\n",
        "    labels=['Low', 'Medium', 'High']\n",
        ")\n",
        "\n",
        "high_risk_products = product_risk[\n",
        "    product_risk['Risk_Level'] == 'High'\n",
        "].copy()\n",
        "\n",
        "high_risk_products = high_risk_products.sort_values(\n",
        "    'Average_Return_Probability',\n",
        "    ascending=False\n",
        ")\n",
        "\n",
        "print(\"High-risk products:\", len(high_risk_products))\n",
        "print(high_risk_products.head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E6IxnHF70axO",
        "outputId": "75cda433-032b-4162-bd60-382216aafae0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "High-risk products: 179\n",
            "     Product_ID Product_Category  Orders  Actual_Returns  \\\n",
            "1124   PROD0276             Toys       1               1   \n",
            "522    PROD0127         Clothing       1               0   \n",
            "1245   PROD0308      Electronics       1               1   \n",
            "1239   PROD0307            Books       1               0   \n",
            "667    PROD0162             Toys       1               0   \n",
            "1066   PROD0262      Electronics       1               0   \n",
            "626    PROD0152  Home Appliances       1               0   \n",
            "90     PROD0022             Toys       1               1   \n",
            "364    PROD0089      Electronics       1               0   \n",
            "320    PROD0078         Clothing       1               0   \n",
            "\n",
            "      Average_Return_Probability  Actual_Return_Rate Risk_Level  \n",
            "1124                    0.608013               100.0       High  \n",
            "522                     0.601916                 0.0       High  \n",
            "1245                    0.589475               100.0       High  \n",
            "1239                    0.589229                 0.0       High  \n",
            "667                     0.588941                 0.0       High  \n",
            "1066                    0.588767                 0.0       High  \n",
            "626                     0.588506                 0.0       High  \n",
            "90                      0.587524               100.0       High  \n",
            "364                     0.587422                 0.0       High  \n",
            "320                     0.583692                 0.0       High  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "high_risk_products.to_csv(\n",
        "    '/content/high_risk_products.csv',\n",
        "    index=False\n",
        ")\n",
        "\n",
        "print(\"Final high-risk products CSV created successfully!\")\n",
        "print(\"Number of high-risk products:\", len(high_risk_products))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qaQuohDi0kOw",
        "outputId": "e567709c-54ea-4b63-c5d6-7d55426de53a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Final high-risk products CSV created successfully!\n",
            "Number of high-risk products: 179\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "fguY9VIM0qtM"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
