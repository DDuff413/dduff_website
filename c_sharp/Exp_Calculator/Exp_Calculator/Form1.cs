using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Exp_Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            decimal[,] expAmounts = new decimal[,] { { numericUpDown1.Value, 10 }, { numericUpDown2.Value, 25 }, { numericUpDown3.Value, 50 },
                                                     { numericUpDown4.Value, 100 }, { numericUpDown5.Value, 200 }, { numericUpDown10.Value, 450 },
                                                     { numericUpDown9.Value, 700 }, { numericUpDown8.Value, 1100 }, { numericUpDown7.Value, 1800 },
                                                     { numericUpDown6.Value, 2300 }, { numericUpDown15.Value, 2900 }, { numericUpDown14.Value, 3900 },
                                                     { numericUpDown13.Value, 5000 }, { numericUpDown12.Value, 5900 }, { numericUpDown11.Value, 7200 },
                                                     { numericUpDown30.Value, 8400 }, { numericUpDown29.Value, 10000 }, { numericUpDown28.Value, 11500 },
                                                     { numericUpDown27.Value, 13000 }, { numericUpDown26.Value, 15000 }, { numericUpDown25.Value, 18000 },
                                                     { numericUpDown24.Value, 20000 }, { numericUpDown23.Value, 22000 }, { numericUpDown22.Value, 25000 },
                                                     { numericUpDown21.Value, 33000 }, { numericUpDown20.Value, 41000 }, { numericUpDown19.Value, 50000 },
                                                     { numericUpDown18.Value, 62000 }, { numericUpDown17.Value, 75000 }, { numericUpDown16.Value, 155000 }
                                                   };
            int totalExp = 0;

            for (int i = 0; i < 30 ; i++)
            {
                totalExp += Decimal.ToInt32(expAmounts[i, 0] * expAmounts[i, 1]);
            }
            try
            {
                totalExp /= Decimal.ToInt32(numericUpDown31.Value);
                textBox1.Text = totalExp.ToString();
            }
            catch (DivideByZeroException)
            {
                textBox1.Text = "0 players";
            }
        }
    }
}
