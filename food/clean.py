import pandas as pd
import json

#read data from csv
data = pd.read_csv('food_dataset.csv',encoding='ISO-8859-1').dropna()

#set data frame for json file
all_data = [{'name':'total',
            'category':'all of them',
            'group':'X',
            'fat':None,
            'protein':None,
            'energy':None,
            'children':[
                {'name':'cereals',
                'category':'cereals and cereal product',
                'group':'A',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'flour',
                     'category':'flour, grains and starches',
                     'group':'AA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'sandwiches',
                     'category':'sandwiches',
                     'group':'AB',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'rice',
                     'category':'rice',
                     'group':'AC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'pasta',
                     'category':'pasta and noodles',
                     'group':'AD',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'pizzas',
                     'category':'pizzas',
                     'group':'AE',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'breads',
                     'category':'breads',
                     'group':'AF',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'rolls',
                     'category':'bread rolls',
                     'group':'AG',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'cereals',
                     'category':'breakfast cereals and porridge',
                     'group':'AI',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'rusks',
                     'category':'infant cereal foods',
                     'group':'AK',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'biscuits',
                     'category':'biscuits, breadsticks and oatcakes',
                     'group':'AM',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'cakes',
                     'category':'cakes and muffins',
                     'group':'AN',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'pastry',
                     'category':'pastry',
                     'group':'AO',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'buns',
                     'category':'buns and pastries',
                     'group':'AP',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'puddings',
                     'category':'puddings',
                     'group':'AS',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'savouries',
                     'category':'savouries',
                     'group':'AT',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'milk',
                'category':'milk and milk product',
                'group':'B',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'cows milk',
                     'category':'cows milk',
                     'group':'BA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'breakfast milk',
                         'category':'breakfast milk',
                         'group':'BAB',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'skimmed milk',
                         'category':'skimmed milk',
                         'group':'BAE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'semi-skimmed milk',
                         'category':'semi-skimmed milk',
                         'group':'BAH',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'whole milk',
                         'category':'whole milk',
                         'group':'BAK',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'processed milks',
                         'category':'processed milks',
                         'group':'BAR',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'other milks',
                     'category':'other milks',
                     'group':'BC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'drinks',
                     'category':'milk-based drinks',
                     'group':'BH',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'creams',
                     'category':'creams',
                     'group':'BJ',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'fresh creams',
                         'category':'fresh creams (pasteurised)',
                         'group':'BJC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'UHT creams',
                         'category':'UHT creams',
                         'group':'BJP',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'imitation creams',
                         'category':'imitation creams',
                         'group':'BJS',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'cheeses',
                     'category':'cheeses',
                     'group':'BL',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'yogurts',
                     'category':'yogurts',
                     'group':'BN',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'whole milk yogurts',
                         'category':'whole milk yogurts',
                         'group':'BNE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'low fat yogurts',
                         'category':'low fat yogurts',
                         'group':'BNH',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'other yogurts',
                         'category':'other yogurts',
                         'group':'BNS',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'ice cream',
                     'category':'ice cream',
                     'group':'BP',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'puddings',
                     'category':'puddings and chilled desserts',
                     'group':'BR',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'fat',
                     'category':'fat spread',
                     'group':'BTM',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'sauces',
                     'category':'savoury dishes and sauces',
                     'group':'BV',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'eggs',
                'category':'eggs',
                'group':'C',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'eggs',
                     'category':'eggs',
                     'group':'CA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'egg dishes',
                     'category':'egg dishes',
                     'group':'CD',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'savoury eggs',
                         'category':'savoury egg dishes',
                         'group':'CDE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'sweet eggs',
                         'category':'sweet egg dishes',
                         'group':'CDH',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    }
                    ]
                },
                {'name':'vegetables',
                'category':'vegetables',
                'group':'D',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'potatoes',
                     'category':'potatoes',
                     'group':'DA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'early potatoes',
                         'category':'early potatoes',
                         'group':'DAE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'main crop potatoes',
                         'category':'main crop potatoes',
                         'group':'DAM',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'chipped old potatoes',
                         'category':'chipped old potatoes',
                         'group':'DAP',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'potato products',
                         'category':'potato products',
                         'group':'DAR',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'beans',
                     'category':'beans and lentils',
                     'group':'DB',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'peas',
                     'category':'peas',
                     'group':'DF',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'vegetables',
                     'category':'vegetables, general',
                     'group':'DG',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'dry vegetables',
                     'category':'vegetables, dried',
                     'group':'DI',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'vegetable dishes',
                     'category':'vegetable dishes',
                     'group':'DR',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'fruit',
                'category':'fruit',
                'group':'F',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'fruit',
                     'category':'fruit, general',
                     'group':'FA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'juices',
                     'category':'fruit juices',
                     'group':'FC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'nuts',
                'category':'nuts and seeds',
                'group':'G',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'nuts, general',
                     'category':'nuts and seeds, general',
                     'group':'GA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'herbs',
                'category':'herbs and spices',
                'group':'H',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[]
                },
                {'name':'fish',
                'category':'fish and fish products',
                'group':'J',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'white fish',
                     'category':'white fish, such as bass and cod',
                     'group':'JA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'fatty fish',
                     'category':'fatty fish, such as salmon and trout',
                     'group':'JC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'crustacea',
                     'category':'crustacea, such as crab and prawns',
                     'group':'JK',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'molluscs',
                     'category':'molluscs, such as calamari and mussels',
                     'group':'JM',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'fish dishes',
                     'category':'fish products and dishes',
                     'group':'JR',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'meat',
                'category':'meat and meat products',
                'group':'M',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'meat',
                     'category':'meat',
                     'group':'MA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'bacon',
                         'category':'bacon',
                         'group':'MAA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'beef',
                         'category':'beef',
                         'group':'MAC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'lamb',
                         'category':'lamb',
                         'group':'MAE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'pork',
                         'category':'pork',
                         'group':'MAG',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'veal',
                         'category':'veal',
                         'group':'MAI',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'poultry',
                     'category':'poultry',
                     'group':'MC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'chicken',
                         'category':'chicken',
                         'group':'MCA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'duck',
                         'category':'duck',
                         'group':'MCC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'goose',
                         'category':'goose',
                         'group':'MCE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'grouse',
                         'category':'grouse',
                         'group':'MCG',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'partridge',
                         'category':'partridge',
                         'group':'MCI',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'pheasant',
                         'category':'pheasant',
                         'group':'MCK',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'pigeon',
                         'category':'pigeon',
                         'group':'MCM',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'turkey',
                         'category':'turkey',
                         'group':'MCO',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'game',
                     'category':'game',
                     'group':'ME',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'hare',
                         'category':'hare',
                         'group':'MEA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'rabbit',
                         'category':'rabbit',
                         'group':'MEC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                        {'name':'venison',
                         'category':'venison',
                         'group':'MEE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                        ]
                    },
                    {'name':'offal',
                     'category':'offal',
                     'group':'MG',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'burgers',
                     'category':'burgers and grillsteaks',
                     'group':'MBG',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'meat products',
                     'category':'meat products, such as sausages',
                     'group':'MI',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                        {'name':'other meat products',
                         'category':'curry, chicken tikka masala',
                         'group':'MIG',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'meat dishes',
                     'category':'meat dishes',
                     'group':'MR',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'fats',
                'category':'fats and oils',
                'group':'O',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'spreading fats',
                     'category':'butter and spreading fats',
                     'group':'OA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'animal fats',
                     'category':'butteroil, unsalted',
                     'group':'OB',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'oils',
                     'category':'oils',
                     'group':'OC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'cooking fats',
                     'category':'cooking fats',
                     'group':'OF',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'beverages',
                'category':'beverages',
                'group':'P',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'powdered drinks',
                     'category':'powdered drinks, essences and infusions',
                     'group':'PA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'powered drinks',
                         'category':'powered drinks and essences',
                         'group':'PAA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'infusions',
                         'category':'coffee and tea',
                         'group':'PAC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'soft drinks',
                     'category':'soft drinks',
                     'group':'PC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'carbonated drinks',
                         'category':'carbonated drinks',
                         'group':'PCA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'squash and cordials',
                         'category':'squash and cordials',
                         'group':'PCC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'juices',
                     'category':'juices',
                     'group':'PE',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'alcohol',
                'category':'alcoholic beverages',
                'group':'Q',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'wines',
                     'category':'wines',
                     'group':'QE',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'fortified wines',
                     'category':'fortified wines',
                     'group':'QF',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'vermouths',
                     'category':'vermouths',
                     'group':'QG',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'liqueurs',
                     'category':'liqueurs',
                     'group':'QI',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                },
                {'name':'snacks',
                'category':'sugar, preserves and snacks',
                'group':'S',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'sugars',
                     'category':'sugars, syrups and preserves',
                     'group':'SC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                    {'name':'confectionery',
                     'category':'confectionery',
                     'group':'SE',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'chocolate confectionery',
                         'category':'chocolate confectionery',
                         'group':'SEA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'non-chocolate',
                         'category':'non-chocolate confectionery',
                         'group':'SEC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'snacks',
                     'category':'savoury snacks',
                     'group':'SN',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'potato snacks',
                         'category':'potato-based snacks',
                         'group':'SNA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'non-potato',
                         'category':'non-potato snacks',
                         'group':'SNC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    }
                    ]
                },
                {'name':'soup',
                'category':'soup and sauses',
                'group':'W',
                'fat':None,
                'protein':None,
                'energy':None,
                'children':[
                    {'name':'soups',
                     'category':'soups',
                     'group':'WA',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'home made',
                         'category':'home made soups',
                         'group':'WAA',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'canned soups',
                         'category':'canned soups',
                         'group':'WAC',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'packet soups',
                         'category':'packet soups',
                         'group':'WAE',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }]
                    },
                    {'name':'sauses',
                     'category':'sauses',
                     'group':'WC',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[
                         {'name':'dairy sauces',
                         'category':'dairy sauces',
                         'group':'WCD',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'salad sauces',
                         'category':'salad sauces, dressings and pickles',
                         'group':'WCG',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        },
                         {'name':'non-salad sauces',
                         'category':'non-salad sauces, including ketchup',
                         'group':'WCN',
                         'fat':None,
                         'protein':None,
                         'energy':None,
                         'children':[]
                        }
                         ]
                    },
                    {'name':'pickles',
                     'category':'pickles and chutneys',
                     'group':'WE',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    },
                   {'name':'miscellaneous foods',
                     'category':'miscellaneous foods, such as salt and yeast',
                     'group':'WY',
                     'fat':None,
                     'protein':None,
                     'energy':None,
                     'children':[]
                    }
                    ]
                }]
            }]

#for parents' data
fat = data['Fat(g)'].astype(float).mean()
pro = data['Protein(g)'].astype(float).mean()
ene = data['Energy(kcal)'].astype(float).mean()
all_data[0]['fat'] = fat
all_data[0]['protein'] = pro
all_data[0]['energy'] = ene

#for children, that is, group of single letter name
for letter in [chr(i) for i in list(range(ord('A'),ord('E'))) + list(range(ord('F'),ord('I'))) + [ord('J')] + [ord('M')] + list(range(ord('O'),ord('R'))) + [ord('S')] + [ord('W')]]:
        data_letter = data[data['Group'].map(lambda x: x.startswith(letter))]
        fat_letter = data_letter['Fat(g)'].astype(float).mean()
        pro_letter = data_letter['Protein(g)'].astype(float).mean()
        ene_letter = data_letter['Energy(kcal)'].astype(float).mean()
        for child in all_data[0]['children']:
            if child['group'] == letter:
                child['fat'] = fat_letter
                child['protein'] = pro_letter
                child['energy'] = ene_letter


#for grandchildren, that is, group of two-letter name (except for 'BTM' and 'MBG')
for word in ['AA','AB','AC','AD','AE','AF','AG','AI','AK','AM','AN','AO','AP','AS','AT','BA','BC','BH','BJ','BL','BN','BP','BR','BTM','BV','CA','CD','DA','DB','DF','DG','DI','DR','FA','FC','GA','JA','JC','JK','JM','JR','MA','MC','ME','MG','MBG','MI','MR','OA','OB','OC','OF','PA','PC','PE','QE','QF','QG','QI','SC','SE','SN','WA','WC','WE','WY']:
    data_word = data[data['Group'].map(lambda x: x.startswith(word))]
    fat_word = data_word['Fat(g)'].astype(float).mean()
    pro_word = data_word['Protein(g)'].astype(float).mean()
    ene_word = data_word['Energy(kcal)'].astype(float).mean()
    for i in all_data[0]['children']:
        for j in range(0,len(i['children'])):
            if i['children'][j]['group'] == word:
                i['children'][j]['fat'] = fat_word
                i['children'][j]['protein'] = pro_word
                i['children'][j]['energy'] = ene_word

#for grand grandchildren, that is, group of three-letter name
for word in ['BAB','BAE','BAH','BAK','BAR','BJC','BJP','BJS','BNE','BNH','BNS','CDE','CDH','DAE','DAM','DAP','DAR','MAA','MAC','MAE','MAG','MAI','MCA','MCC','MCE','MCG','MCI','MCK','MCM','MCO','MEA','MEC','MEE','MIG','PAA','PAC','PCA','PCC','SEA','SEC','SNA','SNC','WAA','WAC','WAE','WCD','WCG','WCN']:
    data_word = data[data['Group'] == word]
    fat_word = data_word['Fat(g)'].astype(float).mean()
    pro_word = data_word['Protein(g)'].astype(float).mean()
    ene_word = data_word['Energy(kcal)'].astype(float).mean()
    for i in all_data[0]['children']:
        for j in range(0,len(i['children'])):
            for k in range(0,len(i['children'][j]['children'])):
                if i['children'][j]['children'][k]['group'] == word:
                    i['children'][j]['children'][k]['fat'] = fat_word
                    i['children'][j]['children'][k]['protein'] = pro_word
                    i['children'][j]['children'][k]['energy'] = ene_word
    
print(json.dumps(all_data, indent=4))

with open('mean.json', 'w') as outfile:
    json.dump(all_data, outfile, indent=4)

