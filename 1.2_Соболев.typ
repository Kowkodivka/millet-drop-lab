#set page(
  paper: "a4",
  margin: (left: 30mm, right: 10mm, top: 20mm, bottom: 20mm),
  numbering: "1",
  number-align: center,
)

#set text(
  font: "Times New Roman",
  size: 14pt,
  lang: "ru",
)

#set par(
  justify: true,
  first-line-indent: 1cm,
  leading: 1em,
)

#set heading(numbering: none)
#set math.equation(numbering: "(1)")

#show heading.where(level: 1): it => {
  v(1.5em, weak: true)
  set text(weight: "bold", size: 14pt)
  pad(left: 1cm)[#it.body]
  v(1em, weak: true)
}
#show figure.where(kind: table): set figure.caption(position: top)
#show figure.where(kind: image): set figure(supplement: "Рисунок")
#show figure.caption: it => {
  set align(if it.kind == table { left } else { center })
  [#it.supplement~#context it.counter.display()~---~#it.body]
}

#page(numbering: none)[
  #set align(center)
  #set par(first-line-indent: 0pt)

  Министерство образования и науки Российской Федерации \
  #v(0.5em)
  *НАЦИОНАЛЬНЫЙ ИССЛЕДОВАТЕЛЬСКИЙ* \
  *ТОМСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ (НИ ТГУ)* \
  #v(0.3em)
  Физический факультет

  #v(4cm)

  #text(size: 17pt, weight: "bold")[ЛАБОРАТОРНАЯ РАБОТА №2] \
  #v(1em)
  #text(size: 17pt)[ПАДЕНИЕ ЖЕЛТОГО ПШЕНА]

  #v(2cm)

  по основной образовательной программе базового высшего образования \
  направление подготовки 09.03.02 --- Информационные системы и технологии \
  программа «Цифровая физика»

  #v(1fr)

  #align(right)[
    #block(width: 7cm)[
      #set align(left)
      Автор работы \
      студент группы № 052603 \
      Соболев Евгений Алексеевич \
      #v(0.5em)
      Дата выполнения: 09.09.2026
    ]
  ]

  #v(1fr)

  Томск --- #datetime.today().year()
]
