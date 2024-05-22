from .element.Day import Day
from .element.Time import Time
from .element.Group import Group
from .element.Shift import Shift

planDeEstudios = [
    [
                {
                    "code": 1803001,
                    "name": "INGLES I",
                    "groups_available": 5,
                    "groups": [
                        Group("CESPEDES GUIZADA MARIA BENITA", "A", "1", [
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.FRIDAY, Time.T0815)
                        ]),
                        Group("CESPEDES GUIZADA MARIA BENITA", "A", "2", [
                            Shift(Day.TUESDAY, Time.T1115),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("PEETERS ILONAA MAGDA LENA", "A", "3", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.WEDNESDAY, Time.T0945)
                        ]),
                        Group("GRILO SALVATIERRA MARIA ESTELA", "A", "4", [
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.FRIDAY, Time.T1415)
                        ]),
                        Group("CESPEDES GUIZADA MARIA BENITA", "A", "5", [
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T1115)
                        ])
                    ]
                },
                {
                    "code": 2006063,
                    "name": "FISICA GENERAL",
                    "groups_available": 1,
                    "groups": [
                        Group("VALENZUELA MIRANDA ROBERTO", "A", "1", [
                            Shift(Day.TUESDAY, Time.T1115),
                            Shift(Day.WEDNESDAY, Time.T1415)
                        ])
                    ]
                }, {
                "code": 2006063,
                "name": "LAB FISICA GENERAL",
                "groups_available": 6,
                "groups": [
                    Group(" MOREIRA CALIZAYA RENE", "A", "B1", [
                        Shift(Day.THURSDAY, Time.T0645)
                    ]),
                    Group("GUZMAN SAAVEDRA ROCIO", "A", "B2", [
                        Shift(Day.THURSDAY, Time.T0815)
                    ]),
                    Group("ORDONEZ SALVATIERRA MIGUEL ANGEL", "A", "B3", [
                        Shift(Day.TUESDAY, Time.T1545)
                    ]),
                    Group("FLORES FLORES FREDDY", "A", "B4", [
                        Shift(Day.MONDAY, Time.T1415)
                    ]),
                    Group("TERRAZAS VARGAS JUAN CARLOS", "A", "B5", [
                        Shift(Day.WEDNESDAY, Time.T1115)
                    ]),
                    Group("TERRAZAS VARGAS JUAN CARLOS", "A", "B6", [
                        Shift(Day.THURSDAY, Time.T1115)
                    ])
                ]
            },
                {
                    "code": 1803001,
                    "name": "ALGEBRA I",
                    "groups_available": 3,
                    "groups": [
                        Group("RODRIGUEZ SEJAS JUAN ANTONIO", "A", "10", [
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.WEDNESDAY, Time.T0815),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("CARRASCO CALVO ALVARO HERNANDO", "A", "15", [
                            Shift(Day.MONDAY, Time.T1715),
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.WEDNESDAY, Time.T1415)
                        ]),
                        Group("LEON ROMERO GUALBERTO", "A", "8", [
                            Shift(Day.WEDNESDAY, Time.T1115),
                            Shift(Day.THURSDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T1415)
                        ])
                    ]
                },
                {
                    "code": 2008054,
                    "name": "CALCULO I",
                    "groups_available": 2,
                    "groups": [
                        Group(" GONZALES CARTAGENA LUCIO", "A", "10", [
                            Shift(Day.WEDNESDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T0645),
                            Shift(Day.SATURDAY, Time.T0945)
                        ]),
                        Group("ROJAS ZURITA RAMIRO", "A", "11", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.THURSDAY, Time.T0815)
                        ])
                    ]
                },
                {
                    "code": 2010010,
                    "name": "INTRODUCCION A LA PROGRAMACION",
                    "groups_available": 8,
                    "groups": [
                        Group("SALAZAR SERRUDO CARLA", "A", "1", [
                            Shift(Day.THURSDAY, Time.T1115),
                            Shift(Day.FRIDAY, Time.T1115),
                            Shift(Day.FRIDAY, Time.T1715)
                        ]),
                        Group("COSTAS JAUREGUI VLADIMIR ABEL", "A", "10", [
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T1415)
                        ]),
                        Group("BLANCO COCA LETICIA", "A", "2", [
                            Shift(Day.TUESDAY, Time.T1715),
                            Shift(Day.WEDNESDAY, Time.T1715),
                            Shift(Day.THURSDAY, Time.T1545)
                        ]),
                        Group("USTARIZ VARGAS HERNAN", "A", "3", [
                            Shift(Day.MONDAY, Time.T1245),
                            Shift(Day.TUESDAY, Time.T1245),
                            Shift(Day.FRIDAY, Time.T1245)
                        ]),
                        Group("VILLARROEL TAPIA HENRY FRANK", "A", "4", [
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.WEDNESDAY, Time.T1545),
                            Shift(Day.SATURDAY, Time.T0945)
                        ]),
                        Group("MONTANO QUIROGA VICTOR HUGO", "A", "5", [
                            Shift(Day.WEDNESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.SATURDAY, Time.T0945)
                        ]),
                        Group("SALAZAR SERRUDO CARLA", "A", "6", [
                            Shift(Day.WEDNESDAY, Time.T1715),
                            Shift(Day.THURSDAY, Time.T1715),
                            Shift(Day.SATURDAY, Time.T0815)
                        ]),
                        Group("FLORES VILLARROEL CORINA", "A", "7", [
                            Shift(Day.TUESDAY, Time.T1245),
                            Shift(Day.THURSDAY, Time.T0815),
                            Shift(Day.FRIDAY, Time.T0815)
                        ])
                    ]
                },

            ],
            [
                {
                    "code": 1803002,
                    "name": "INGLES II",
                    "groups_available": 3,
                    "groups": [
                        Group("PEETERS ILONAA MAGDA LENA", "B", "1", [
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T0645)
                        ]),
                        Group("PEETERS ILONAA MAGDA LENA", "B", "2", [
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("PEETERS ILONAA MAGDA LENA", "B", "3", [
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T0645)
                        ])
                    ]
                },
                {
                    "code": 2008022,
                    "name": "ALGEBRA II",
                    "groups_available": 3,
                    "groups": [
                        Group("SALINAS PERICON WALTER OSCAR", "B", "5A", [
                            Shift(Day.MONDAY, Time.T1715),
                            Shift(Day.TUESDAY, Time.T1715),
                            Shift(Day.THURSDAY, Time.T1845)
                        ]),
                        Group("SILVA RAMOS HERNAN VICTOR", "B", "6", [
                            Shift(Day.THURSDAY, Time.T1545),
                            Shift(Day.FRIDAY, Time.T1715),
                            Shift(Day.SATURDAY, Time.T0945)
                        ]),
                        Group("OMONTE OJALVO JOSE ROBERTO", "B", "8", [
                            Shift(Day.MONDAY, Time.T1115),
                            Shift(Day.TUESDAY, Time.T1415),
                            Shift(Day.THURSDAY, Time.T1545)
                        ])
                    ]
                },
                {
                    "code": 2008056,
                    "name": "CALCULO II",
                    "groups_available": 2,
                    "groups": [
                        Group("MARTINEZ MAIDA AMILCAR SAUL", "B", "12", [
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.WEDNESDAY, Time.T1415),
                            Shift(Day.FRIDAY, Time.T1245)
                        ]),
                        Group("TERRAZAS LOBO JUAN", "B", "6", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.MONDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T1415),
                            Shift(Day.THURSDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T1415)
                        ])
                    ]
                },
                {
                    "code": 2010003,
                    "name": "ELEM. DE PROGRAMACION Y ESTRUC. DE DATOS",
                    "groups_available": 4,
                    "groups": [
                        Group("TORRICO BASCOPE ROSEMARY", "B", "1", [
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T1115),
                            Shift(Day.FRIDAY, Time.T0815)
                        ]),
                        Group("BLANCO COCA LETICIA", "B", "2", [
                            Shift(Day.MONDAY, Time.T1245),
                            Shift(Day.WEDNESDAY, Time.T1545),
                            Shift(Day.THURSDAY, Time.T1245)
                        ]),
                        Group("BLANCO COCA LETICIA", "B", "3", [
                            Shift(Day.TUESDAY, Time.T1845),
                            Shift(Day.WEDNESDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T1245)
                        ]),
                        Group("TORRICO BASCOPE ROSEMARY", "B", "5", [
                            Shift(Day.MONDAY, Time.T1245),
                            Shift(Day.MONDAY, Time.T1545),
                            Shift(Day.WEDNESDAY, Time.T0945)
                        ])
                    ]
                },
                {
                    "code": 2010013,
                    "name": "ARQUITECTURA DE COMPUTADORAS I",
                    "groups_available": 2,
                    "groups": [
                        Group("ACHA PEREZ SAMUEL", "B", "1", [
                            Shift(Day.THURSDAY, Time.T0645),
                            Shift(Day.SATURDAY, Time.T0645)
                        ]),
                        Group("BLANCO COCA LETICIA", "B", "2", [
                            Shift(Day.MONDAY, Time.T1415),
                            Shift(Day.THURSDAY, Time.T1415)
                        ])
                    ]
                },
                {
                    "code": 2010200,
                    "name": "PROGRAMACION",
                    "groups_available": 1,
                    "groups": [
                        Group("TORRICO BASCOPE ROSEMARY", "B", "1", [
                            Shift(Day.MONDAY, Time.T1115),
                            Shift(Day.WEDNESDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T1115)
                        ])
                    ]
                }
            ],
            [
                {
                    "code": 2008060,
                    "name": "CALCULO NUMERICO",
                    "groups_available": 2,
                    "groups": [
                        Group("JUCHANI BAZUALDO DEMETRIO", "C", "2", [
                            Shift(Day.MONDAY, Time.T1415),
                            Shift(Day.TUESDAY, Time.T1115),
                            Shift(Day.THURSDAY, Time.T0645)
                        ]),
                        Group("ZABALAGA MONTANO OSCAR A.", "C", "3", [
                            Shift(Day.MONDAY, Time.T0815),
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.WEDNESDAY, Time.T1545)
                        ])
                    ]
                },
                {
                    "code": 2008140,
                    "name": "LOGICA",
                    "groups_available": 1,
                    "groups": [
                        Group("HOEPFNER REYNOLDS MAURICIO", "C", "1", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T1415)
                        ])
                    ]
                },
                {
                    "code": 2010014,
                    "name": "ARQUITECTURA DE COMPUTADORAS II",
                    "groups_available": 1,
                    "groups": [
                        Group("AGREDA CORRALES LUIS ROBERTO", "C", "1", [
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.THURSDAY, Time.T1715)
                        ])
                    ]
                },
                {
                    "code": 2010037,
                    "name": "TEORIA DE GRAFOS",
                    "groups_available": 1,
                    "groups": [
                        Group("MONTOYA BURGOS YONY RICHARD", "C", "1", [
                            Shift(Day.MONDAY, Time.T1545),
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.THURSDAY, Time.T1245)
                        ])
                    ]
                },
                {
                    "code": 2010041,
                    "name": "ORGANIZACION Y METODOS",
                    "groups_available": 1,
                    "groups": [
                        Group("CAMACHO DEL CASTILLO INDIRA", "C", "1", [
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.THURSDAY, Time.T0815)
                        ])
                    ]
                },
                {
                    "code": 2010206,
                    "name": "METODOS Y TECNICAS DE PROGRAMACION",
                    "groups_available": 3,
                    "groups": [
                        Group("FLORES VILLARROEL CORINA", "C", "1", [
                            Shift(Day.MONDAY, Time.T1115),
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T0815)
                        ]),
                        Group("MANZUR SORIA CARLOS B", "C", "2", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T0645),
                            Shift(Day.SATURDAY, Time.T0645)
                        ]),
                        Group("MONTOYA BURGOS YONY RICHARD", "C", "5", [
                            Shift(Day.MONDAY, Time.T1845),
                            Shift(Day.TUESDAY, Time.T1845),
                            Shift(Day.WEDNESDAY, Time.T1545)
                        ])
                    ]
                }],
            [
                {
                    "code": 2008029,
                    "name": "PROBABILIDAD Y ESTADISTICA",
                    "groups_available": 2,
                    "groups": [
                        Group("DELGADILLO COSSIO DAVID ALFREDO", "D", "3", [
                            Shift(Day.MONDAY, Time.T1715),
                            Shift(Day.TUESDAY, Time.T1715),
                            Shift(Day.WEDNESDAY, Time.T1715)
                        ]),
                        Group("OMONTE OJALVO JOSE ROBERTO", "D", "4", [
                            Shift(Day.MONDAY, Time.T0945),
                            Shift(Day.TUESDAY, Time.T1245),
                            Shift(Day.FRIDAY, Time.T0945)
                        ])
                    ]
                },
                {
                    "code": 2010005,
                    "name": "TALLER DE PROGRAMACION EN BAJO NIVEL",
                    "groups_available": 1,
                    "groups": [
                        Group("MONTECINOS CHOQUE MARCO ANTONIO", "D", "1", [
                            Shift(Day.TUESDAY, Time.T1545),
                            Shift(Day.WEDNESDAY, Time.T1545),
                            Shift(Day.THURSDAY, Time.T1545)
                        ])
                    ]
                },
                {
                    "code": 2010005,
                    "name": "BASE DE DATOS I",
                    "groups_available": 2,
                    "groups": [
                        Group("APARICIO YUJA TATIANA", "D", "1", [
                            Shift(Day.TUESDAY, Time.T1245),
                            Shift(Day.WEDNESDAY, Time.T1245),
                            Shift(Day.THURSDAY, Time.T1245)
                        ]),
                        Group("CALANCHA NAVIA BORIS", "D", "2", [
                            Shift(Day.TUESDAY, Time.T2015),
                            Shift(Day.WEDNESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T1245)
                        ])
                    ]
                },
                {
                    "code": 2010018,
                    "name": "SISTEMAS DE INFORMACION I",
                    "groups_available": 2,
                    "groups": [
                        Group("SALAZAR SERRUDO CARLA", "D", "1", [
                            Shift(Day.WEDNESDAY, Time.T1545),
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("SALAZAR SERRUDO CARLA", "D", "2", [
                            Shift(Day.MONDAY, Time.T1715),
                            Shift(Day.TUESDAY, Time.T1715),
                            Shift(Day.WEDNESDAY, Time.T1115)
                        ])
                    ]
                },
                {
                    "code": 2010038,
                    "name": "PROGRAMACION FUNCIONAL",
                    "groups_available": 1,
                    "groups": [
                        Group("APARICIO YUJA TATIANA", "D", "1", [
                            Shift(Day.MONDAY, Time.T0815),
                            Shift(Day.TUESDAY, Time.T1415),
                            Shift(Day.WEDNESDAY, Time.T0645)
                        ])
                    ]
                },
                {
                    "code": 2010197,
                    "name": "ALGORITMOS AVANZADOS",
                    "groups_available": 1,
                    "groups": [
                        Group("BLANCO COCA LETICIA", "D", "1", [
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T0645)
                        ])
                    ]
                }
            ],
            [
                {
                    "code": 2010016,
                    "name": "BASE DE DATOS II",
                    "groups_available": 2,
                    "groups": [
                        Group("APARICIO YUJA TATIANA", "E", "1", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.WEDNESDAY, Time.T0815)
                        ]),
                        Group("APARICIO YUJA TATIANA", "E", "2", [
                            Shift(Day.MONDAY, Time.T1245),
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T0945)
                        ])
                    ]
                },
                {
                    "code": 2010017,
                    "name": "TALLER DE SISTEMAS OPERATIVOS",
                    "groups_available": 2,
                    "groups": [
                        Group("ORELLANA ARAOZ JORGE WALTER", "E", "1", [
                            Shift(Day.TUESDAY, Time.T1715),
                            Shift(Day.WEDNESDAY, Time.T1415),
                            Shift(Day.FRIDAY, Time.T1415)
                        ]),
                        Group("ORELLANA ARAOZ JORGE WALTER", "E", "2", [
                            Shift(Day.WEDNESDAY, Time.T0815),
                            Shift(Day.THURSDAY, Time.T1715),
                            Shift(Day.FRIDAY, Time.T0815)
                        ]),
                        Group("CUSSI NICOLAS GROVER HUMBERTO", "E", "3", [
                            Shift(Day.TUESDAY, Time.T1845),
                            Shift(Day.THURSDAY, Time.T2015),
                            Shift(Day.SATURDAY, Time.T0815)
                        ])
                    ]
                }, {
                "code": 2010022,
                "name": "SISTEMAS DE INFORMACION II",
                "groups_available": 2,
                "groups": [
                    Group("FLORES SOLIZ JUAN MARCELO", "E", "1", [
                        Shift(Day.TUESDAY, Time.T0645),
                        Shift(Day.WEDNESDAY, Time.T0645),
                        Shift(Day.FRIDAY, Time.T0645)
                    ]),
                    Group("JALDIN ROSALES K. ROLANDO", "E", "2", [
                        Shift(Day.WEDNESDAY, Time.T0815),
                        Shift(Day.THURSDAY, Time.T1715),
                        Shift(Day.FRIDAY, Time.T1545)
                    ])
                ]
            },
                {
                    "code": 2010040,
                    "name": "TEORIA DE AUTOMATAS Y LENG. FORMALES",
                    "groups_available": 1,
                    "groups": [
                        Group("MONTANO QUIROGA VICTOR HUGO", "E", "1", [
                            Shift(Day.MONDAY, Time.T0945),
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0815)
                        ])
                    ]
                }, {
                "code": 2010042,
                "name": "GRAFICACION POR COMPUTADORA",
                "groups_available": 1,
                "groups": [
                    Group("CALANCHA NAVIA BORIS", "E", "1", [
                        Shift(Day.MONDAY, Time.T1115),
                        Shift(Day.TUESDAY, Time.T1245),
                        Shift(Day.WEDNESDAY, Time.T1545)
                    ])
                ]
            }, {
                "code": 2010201,
                "name": "INTELIGENCIA ARTIFICIAL I",
                "groups_available": 2,
                "groups": [
                    Group("GARCIA PEREZ CARMEN ROSA", "E", "1", [
                        Shift(Day.TUESDAY, Time.T1115),
                        Shift(Day.WEDNESDAY, Time.T0945),
                        Shift(Day.THURSDAY, Time.T1115)
                    ]),
                    Group("RODRIGUEZ BILBAO ERIKA PATRICIA", "E", "2", [
                        Shift(Day.MONDAY, Time.T1845),
                        Shift(Day.TUESDAY, Time.T1545),
                        Shift(Day.WEDNESDAY, Time.T1715)
                    ])
                ]
            }
            ], [
                {
                    "code": 2010020,
                    "name": "INGENIERIA DE SOFTWARE",
                    "groups_available": 2,
                    "groups": [
                        Group("CAMACHO DEL CASTILLO INDIRA", "F", "1", [
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.WEDNESDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T0645)
                        ]),
                        Group("TORRICO BASCOPE ROSEMARY", "F", "2", [
                            Shift(Day.TUESDAY, Time.T1115),
                            Shift(Day.WEDNESDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0945)
                        ])
                    ]
                }, {
                    "code": 2010047,
                    "name": "REDES DE COMPUTADORAS",
                    "groups_available": 2,
                    "groups": [
                        Group("ORELLANA ARAOZ JORGE WALTER", "F", "1", [
                            Shift(Day.MONDAY, Time.T1415),
                            Shift(Day.WEDNESDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("ORELLANA ARAOZ JORGE WALTER", "F", "2", [
                            Shift(Day.MONDAY, Time.T0945),
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T0945)
                        ])
                    ]
                },
                {
                    "code": 2010049,
                    "name": "ESTRUCTURA Y SEMANTICA DE LENGUAJES DE",
                    "groups_available": 1,
                    "groups": [
                        Group("ROMERO RODRIGUEZ PATRICIA", "F", "1", [
                            Shift(Day.MONDAY, Time.T1115),
                            Shift(Day.TUESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T1115)
                        ])
                    ]
                }, {
                    "code": 2010053,
                    "name": "TALLER DE BASE DE DATOS",
                    "groups_available": 3,
                    "groups": [
                        Group("CALANCHA NAVIA BORIS", "F", "1", [
                            Shift(Day.THURSDAY, Time.T1115),
                            Shift(Day.FRIDAY, Time.T0645)
                        ]),
                        Group("CALANCHA NAVIA BORIS", "F", "2", [
                            Shift(Day.WEDNESDAY, Time.T2015),
                            Shift(Day.THURSDAY, Time.T0645)
                        ]),
                        Group("FLORES SOLIZ JUAN MARCELO", "F", "3", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T0645)
                        ])
                    ]
                }, {
                    "code": 2010202,
                    "name": "INTELIGENCIA ARTIFICIAL II",
                    "groups_available": 1,
                    "groups": [
                        Group("GARCIA PEREZ CARMEN ROSA", "F", "1", [
                            Shift(Day.TUESDAY, Time.T1245),
                            Shift(Day.WEDNESDAY, Time.T1115),
                            Shift(Day.THURSDAY, Time.T1245)
                        ])
                    ]
                }, {
                    "code": 2010202,
                    "name": "PROGRAMACION WEB",
                    "groups_available": 1,
                    "groups": [
                        Group("COSTAS JAUREGUI VLADIMIR ABEL", "F", "1", [
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T0945),
                            Shift(Day.THURSDAY, Time.T0815)
                        ])
                    ]
                }
            ], [
                {
                    "code": 2010019,
                    "name": "SIMULACION DE SISTEMAS",
                    "groups_available": 1,
                    "groups": [
                        Group("VILLARROEL TAPIA HENRY FRANK", "G", "1", [
                            Shift(Day.MONDAY, Time.T1545),
                            Shift(Day.TUESDAY, Time.T1715)
                        ])
                    ]
                }, {
                    "code": 2010024,
                    "name": "TALLER DE INGENIERIA DE SOFTWARE",
                    "groups_available": 2,
                    "groups": [
                        Group("FLORES VILLARROEL CORINA", "G", "1", [
                            Shift(Day.MONDAY, Time.T0945),
                            Shift(Day.TUESDAY, Time.T0945)
                        ]),
                        Group("BLANCO COCA LETICIA", "G", "2", [
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T0815)
                        ])
                    ]
                }, {
                    "code": 2010100,
                    "name": "ARQUITECTURA DE SOFTWARE",
                    "groups_available": 1,
                    "groups": [
                        Group("AZERO ALCOCER PABLO", "G", "1", [
                            Shift(Day.MONDAY, Time.T1415),
                            Shift(Day.THURSDAY, Time.T0645),
                            Shift(Day.FRIDAY, Time.T1545)
                        ])
                    ]
                }, {
                    "code": 2010204,
                    "name": "INTERACCION HUMANO COMPUTADOR",
                    "groups_available": 1,
                    "groups": [
                        Group("FLORES VILLARROEL CORINA", "G", "1", [
                            Shift(Day.TUESDAY, Time.T0645),
                            Shift(Day.THURSDAY, Time.T1845)
                        ])
                    ]
                },
                {
                    "code": 2010205,
                    "name": "TECNOLOGIA REDES AVANZADAS",
                    "groups_available": 1,
                    "groups": [
                        Group("MONTECINOS CHOQUE MARCO ANTONIO", "G", "1", [
                            Shift(Day.TUESDAY, Time.T1415),
                            Shift(Day.WEDNESDAY, Time.T1415),
                            Shift(Day.THURSDAY, Time.T1415)
                        ])
                    ]
                }
            ], [
                {
                    "code": 2010035,
                    "name": "APLICACION DE SISTEMAS OPERATIVOS",
                    "groups_available": 2,
                    "groups": [
                        Group("CUSSI NICOLAS GROVER HUMBERTO", "H", "1", [
                            Shift(Day.FRIDAY, Time.T1845),
                            Shift(Day.SATURDAY, Time.T0945)
                        ]),
                        Group("CUSSI NICOLAS GROVER HUMBERTO", "H", "2", [
                            Shift(Day.MONDAY, Time.T1245),
                            Shift(Day.THURSDAY, Time.T1845)
                        ])
                    ]
                }, {
                    "code": 2010102,
                    "name": "EVALUACION Y AUDITORIA DE SISTEMAS",
                    "groups_available": 2,
                    "groups": [
                        Group("ROMERO RODRIGUEZ PATRICIA", "H", "1", [
                            Shift(Day.TUESDAY, Time.T1115),
                            Shift(Day.WEDNESDAY, Time.T0815),
                            Shift(Day.THURSDAY, Time.T0815)
                        ]),
                        Group("VILLARROEL NOVILLO JIMMY", "H", "2", [
                            Shift(Day.MONDAY, Time.T0645),
                            Shift(Day.TUESDAY, Time.T0815),
                            Shift(Day.WEDNESDAY, Time.T0645)
                        ])
                    ]
                }, {
                    "code": 2010214,
                    "name": "TALLER DE GRADO I",
                    "groups_available": 2,
                    "groups": [
                        Group("FLORES VILLARROEL CORINA", "H", "1", [
                            Shift(Day.WEDNESDAY, Time.T1115),
                            Shift(Day.THURSDAY, Time.T0945),
                            Shift(Day.FRIDAY, Time.T0945)
                        ]),
                        Group("ROMERO RODRIGUEZ PATRICIA", "H", "2", [
                            Shift(Day.MONDAY, Time.T0945),
                            Shift(Day.WEDNESDAY, Time.T1115),
                            Shift(Day.THURSDAY, Time.T0945)
                        ])
                    ]
                }
            ]
]
