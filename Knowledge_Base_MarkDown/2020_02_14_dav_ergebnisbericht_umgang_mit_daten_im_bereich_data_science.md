# 2020-02-14_DAV-Ergebnisbericht_Umgang_mit_Daten_im_Bereich_Data_Science

## Page 1
# DAV 

DEUTSCHE
AKTUARVEREINIGUNG e.V.

Ergebnisbericht des Ausschusses Actuarial Data Science

## Umgang mit Daten im Bereich Data Science

Köln, 14. Februar 2020

## Page 2
# Präambel 

Der Ausschuss Actuarial Data Science der Deutschen Aktuarvereinigung e. V. (DAV) hat den vorliegenden Ergebnisbericht erstellt.

## Zusammenfassung

Der Ergebnisbericht behandelt Prinzipien sowie ethische Leitlinien im Umgang mit Daten aufbauend auf den Standesregeln der DAV und den einschlägigen Gesetzen in diesem Bereich. Insbesondere werden Prinzipien im Umgang mit personenbezogenen Daten der besonderen Kategorie behandelt und Hilfestellungen zur Verwendung von Methoden und Tools im Umgang mit Daten gegeben.

Aktuare (hier und nachfolgend seien damit die Mitglieder der Deutschen Aktuarvereinigung e.V., DAV, bezeichnet) sind durch ihre grundlegenden Fähigkeiten in Mathematik, Statistik und auch in Programmiersprachen gut vorbereitet, die neuen Ansätze im Bereich Data Science zu verfolgen und diese nachzuvollziehen. Die stetige Entwicklung setzt eine permanente Weiterbildung und das Erlernen neuer Fähigkeiten voraus. Sie stellt Aktuare vor eine Vielzahl von berufsständischen Fragestellungen.

Die in dem Ergebnisbericht gegebenen nachfolgenden Hilfestellungen im Umgang mit Daten im Bereich Data Science beinhalten ergänzend zu den Standesregeln für Aktuare in der DAV allgemeine Prinzipien und ethische Grundsätze im Bereich Data Science. Sie dienen als Hilfestellung im Umgang mit Daten und den hierzu verwendeten Tools und Methoden.

Das Folgende versteht sich unter der Voraussetzung, dass die Arbeitgeber von Aktuaren (z.B. Versicherungsunternehmen) alle nötigen fachlichen und organisatorischen Vorkehrungen im Rahmen gesetzlicher Vorgaben (z.B. der EUDatenschutzgrundverordnung) getroffen haben und dass die Aktuare von ihren Arbeitgebern entsprechend geschult wurden. Die in diesem Zusammenhang verschiedentlich Aktuaren auch außerhalb ihrer Kernaufgaben zugesprochenen Rollen werden hier nicht explizit genannt, da diese von Unternehmen zu Unternehmen sehr verschieden sind.

Die EU-Datenschutzgrundverordnung (DSGVO) sowie das Bundesdatenschutzgesetz bleiben von den folgenden Grundsätzen unberührt.

Der Ergebnisbericht ist an die Mitglieder und Gremien der DAV zur Information über den Stand der Diskussion und die erzielten Erkenntnisse gerichtet und stellt keine berufsständisch legitimierte Position der DAV dar. ${ }^{1}$

[^0]
[^0]:    ${ }^{1}$ Die sachgemäße Anwendung des Ergebnisberichts erfordert aktuarielle Fachkenntnisse. Dieser Ergebnisbericht stellt deshalb keinen Ersatz für entsprechende professionelle aktuarielle Dienstleistungen dar. Aktuarielle Entscheidungen mit Auswirkungen auf persönliche Vorsorge und Absicherung, Kapitalanlage oder geschäftliche Aktivitäten sollten ausschließlich auf Basis der Beurteilung durch eine(n) qualifizierte(n) Aktuar DAV/Aktuarin DAV getroffen werden.

## Page 3
# Verabschiedung 

Dieser Ergebnisbericht ist durch den Ausschuss Actuarial Data Science am 14. Februar 2020 verabschiedet worden.

## Page 4
# Inhalt 

1. Allgemeine Prinzipien im Umgang mit Daten und Compliance ..... 5
2. Prinzipien im Umgang mit personenbezogenen Daten ..... 7
3. Erhebung und Verarbeitung von besonderen Kategorien personenbezogener Daten ..... 8
4. Diskriminierung ..... 9
5. Datenschutzbeauftragter ..... 10
6. Verwendung von Modellen, Methoden und Tools im Umgang mit Daten ..... 11
Quellen ..... 13

## Page 5
# 1. Allgemeine Prinzipien im Umgang mit Daten und Compliance 

1.1. Aktuare sind gemäß Artikel 9.1 der Standesregeln² dazu verpflichtet, gesetzeskonform zu handeln. Dies bezieht sich im Bereich Data Science insbesondere auf die Einhaltung der europäischen Richtlinien und der deutschen Gesetze im Umfeld des Datenschutzes. ${ }^{3}$ Sie sind auch verpflichtet, sich bzgl. der Gesetze und Richtlinien auf dem neuesten Stand zu halten.
1.2. Aktuare stellen innerhalb ihres Arbeitsgebiets damit sicher, dass die gesetzlichen Regelungen in der Erhebung, Speicherung, Zugriffskontrolle und Verarbeitung der Daten, der Wissensgenerierung und der Nutzung des generierten Wissens im konkreten Kontext von Daten eingehalten werden.
1.3. Soweit dies im Unternehmen nicht bereits klar geregelt ist, kommunizieren und dokumentieren Aktuare innerhalb ihrer Prozesse die Herkunft der Daten und deren Verwendung. Sie dokumentieren die durchgeführten Kontrollen und Ergebnisse ihrer Tätigkeit, dabei verdeutlichen sie den Umfang sowie die Grenzen ihrer Ergebnisse und zeigen die Einschränkungen durch die Annahmen auf.
1.4. Aktuare sind sich darüber bewusst, dass bei der Auswertung der Daten gefundenen Korrelationen mehrere Ursachen zu Grunde liegen können und sich aus Korrelationen nicht zwingend Kausalitäten ergeben. Sie sind sich auch darüber bewusst, dass es bei versicherungstechnischen Fragestellungen - im Gegensatz zu vielen anderen Fragestellungen mit Einsatz großer Datenmengen - sehr oft zu einem großen time-lag zwischen Datenerhebung und Anwendungszeitraum der gefundenen Ergebnisse kommt und müssen daher im Besonderen Änderungs- und Irrtumswahrscheinlichkeiten beachten und diese kommunizieren.
1.5. Aktuare verfügen gemäß Artikel 2.3. und 3. der Standesregeln ${ }^{4,5}$ über die nötigen Fähigkeiten im Umgang mit Daten (insbesondere in Bezug auf personenbezogene Daten) und stellen sicher, dass ihre Kenntnisse und Fähigkeiten für die notwendigen Methoden und Tools auf dem aktuellen Stand sind. Das bedeutet insbesondere, dass sie in der Lage sind, die verwendeten Methoden der Aufgabenstellung anzupassen.

[^0]
[^0]:    ${ }^{2}$ Artikel 9.1.: Aktuare üben ihre berufliche Tätigkeit im Einklang mit den gesetzlichen und aufsichtsrechtlichen Vorgaben aus.
    ${ }^{3}$ Als Hilfestellung kann hier zum Beispiel die Ausarbeitung der AAE „GDPR from an actuarial perspective" dienen.
    ${ }^{4}$ Artikel 2.3.: Aktuare üben ihre berufliche Tätigkeit nur aus, wenn sie hierfür fachlich kompetent sind und über hinreichende Erfahrung verfügen.
    ${ }^{5}$ Artikel 3.: Aktuare haben ihre Tätigkeit in eigener Verantwortung und nach bestem Wissen auszuüben. Sie sind dafür verantwortlich, sich den für ihre Berufsausübung erforderlichen aktuellen Kenntnisstand durch entsprechende Weiterbildung zu erhalten, und sie sind dazu verpflichtet, die jeweils geltende Weiterbildungsordnung einzuhalten. Sie tragen die Verantwortung für eine ordnungsgemäße und gesetzeskonforme Erfüllung aller Leistungen, die im Zusammenhang mit aktuariellen Tätigkeiten von ihnen oder ihren Beauftragten erbracht werden. Hierzu gehören Qualitätssicherungsmaßnahmen sowie die Sicherstellung ausreichender Kapazitäten.

## Page 6
1.6. Aktuare sind gemäß Artikel 4.3. der Standesregeln ${ }^{6}$ in der Lage, die Ergebnisse und Folgerungen der Anwendung neuer statistischer Methoden auf Daten gegenüber Dritten verfahrensspezifisch zu erklären.
[^0]
[^0]:    ${ }^{6}$ Artikel 4.3.: Aktuare berücksichtigen die Kenntnisse, das Verständnis und den Umfang des relevanten Fachwissens sowie den Bedarf des vorgesehenen Nutzers, damit dieser die Auswirkungen der Kommunikation des Aktuars verstehen kann:
    Form und Inhalt: Aktuare bestimmen Form, Struktur, Stil, Detaillierungsgrad und Inhalt der Kommunikation unter Berücksichtigung des vorgesehenen Nutzers so, dass sie für die jeweiligen Umstände geeignet sind. Klarheit: Aktuare verwenden klare Formulierungen unter Berücksichtigung des vorgesehenen Nutzers und wählen eine Ausdrucksform, die für die jeweiligen Umstände geeignet ist.

## Page 7
# 2. Prinzipien im Umgang mit personenbezogenen Daten 

2.1. Aktuare sind mit den Risiken bei der Verwendung von personenbezogenen Daten vertraut. Sie ergreifen alle ihnen möglichen Maßnahmen zum Schutz der Daten und zur Begrenzung des Missbrauchsrisikos. Die folgenden Punkte spezifizieren Verantwortlichkeiten soweit Aktuare innerhalb ihrer Prozesse die Datenhoheit innehaben.
2.2. Aktuare verwenden im Zuge der im Unternehmen kodifizierten und überwachten Complianceregeln personenbezogene Daten nur für die der betroffenen Person bekannten Zwecke. Dementsprechend werden die Zweckbestimmungen nur sofern dies rechtlich zulässig ist geändert bzw. erweitert und die betroffenen Personen entsprechend informiert.
2.3. Soweit nicht ohnehin im Unternehmen definierte Prozesse befolgt werden, gewährleisten Aktuare bei der Verwendung personenbezogener Daten, dass die Herkunft der Daten erkennbar bzw. dokumentiert ist, die Risiken in der Verwendung von personenbezogenen Daten bekannt sind und der Datenschutzbeauftragte (DSB) über deren Verwendung informiert ist.
2.4. Im Rahmen der Governance ihrer Unternehmen beachten Aktuare bei der Verarbeitung von personenbezogenen Daten den Grundsatz der Datenminimierung (Art. 5 Abs. 1 lit c) DSGVO) und der Speicherbegrenzung (Art. 5 Abs. 1 lit e) DSGVO). Dabei speichern Aktuare personenbezogene Daten in einer Form, die die Identifizierung der betroffenen Person nur so lange ermöglicht, wie es für die Zwecke (vorbehaltlich von statistischen Zwecken, für im öffentlichen Interesse liegende Archivzwecke oder für wissenschaftliche und historische Zwecke gemäß Art. 5 Abs. 1 lit e) DSGVO) erforderlich ist. Insofern möglich, anonymisieren oder pseudonymisieren Aktuare Daten. Aktuare ziehen dabei soweit möglich und notwendig eine Anonymisierung einer Pseudonymisierung der Daten vor.
2.5. Aktuare stellen gemäß Art. 5 Abs. 1 lit. d) sicher, dass personenbezogene Daten richtig und falls erforderlich auf dem neuesten Stand sind. Sie informieren die zuständigen Stellen, dass personenbezogene Daten, die in Hinblick auf ihre Zwecke unrichtig sind, unverzüglich korrigiert, gelöscht oder deren Verarbeitung eingeschränkt wird.
2.6. Insofern eine Einwilligung zur Verarbeitung personenbezogener Daten notwendig ist, erfragen Aktuare beim Datenschutzbeauftragten (soweit dies nicht ohnehin in den Prozessen des Unternehmens vorgesehen und ersichtlich ist), dass die Einwilligung noch nicht widerrufen wurde und diese freiwillig, in informierter Weise und unmissverständlich erfolgt ist.
2.7. Falls der Versuch eines Diebstahls oder einer Veruntreuung von personenbezogenen Daten festgestellt wird und dieser nicht selbstständig behoben werden kann, geben Aktuare die Information an die entsprechenden Ansprechpartner weiter.

## Page 8
# 3. Erhebung und Verarbeitung von besonderen Kategorien personenbezogener Daten 

3.1. Aktuare erheben und verarbeiten im Rahmen der Complianceregeln ihres Unternehmens personenbezogene Daten der besonderen Kategorien gemäß Art. 9 Abs. 1 DSGVO nur, wenn eine gesetzliche Grundlage gegeben ist oder ihnen eine ausdrückliche Einwilligung der betroffenen Person zur Verwendung dieser Daten vorliegt.
3.2. Erhebung ${ }^{7}$ und Verarbeitung von Gesundheitsdaten
3.2.1. Aktuare verwenden ohne ausdrückliche Einwilligung der betroffenen Person keine Gesundheitsdaten, hiervon ausgenommen sind Daten, die bereits im Vorfeld anonymisiert wurden.
3.2.2. Bestehen bei nicht-anonymisierten Gesundheitsdaten Zweifel über die Einwilligung der betroffenen Person, werden Aktuare dies beim Datenschutzbeauftragten melden und gegebenenfalls zur Vernichtung der Daten angemessen beitragen.
3.2.3. Aktuare tragen aktiv dazu bei, den Schutz der Gesundheitsdaten zu gewährleisten. Sie stellen im Rahmen ihrer Analysen sicher, dass die Gesundheitsdaten gemäß geltender Vorschriften und besonders sorgfältig verarbeitet werden.
3.2.4. Aktuare halten die Verschwiegenheitsverpflichtung gemäß Artikel 7 der Standesregeln ${ }^{8}$ ein.
3.2.5. Sie verpflichten sich, auf festgestellte Ausfallrisiken im Umgang mit den Daten hinzuweisen und die Behebung der Risiken vorzuschlagen.
3.2.6. Insofern ein Zugriff auf nicht-anonymisierte Gesundheitsdaten notwendig ist, veranlassen Aktuare mittels der im Unternehmen dafür vorgesehenen Wege, dass eine entsprechende Einwilligung der betroffenen Person eingeholt wird.

[^0]
[^0]:    ${ }^{7}$ Bei der Erhebung von Gesundheitsdaten ist § 213 VVG zu beachten. Darüber hinaus ist in § 203 StGB das Thema „Verletzung von Privatgeheimnissen" geregelt.
    ${ }^{8}$ Artikel 7: Aktuare dürfen gegenüber anderen Parteien keine vertraulichen Informationen, die ihnen im Rahmen ihrer Berufsausübung anvertraut oder bekannt geworden sind, offenlegen, es sei denn, der Auftrag- oder Arbeitgeber hat sie von ihrer Verschwiegenheitspflicht entbunden oder die Offenlegung wird aufgrund rechtlicher Vorgaben gefordert.

## Page 9
# 4. Diskriminierung 

4.1. In § 20 Abs. 2 AGG wird explizit die unterschiedliche Behandlung wegen Religion, Behinderung, Alter oder sexueller Identität bei Versicherungen erlaubt, wenn sie „auf anerkannten Prinzipien risikoadäquater Kalkulation beruht, insbesondere auf einer versicherungsmathematisch ermittelten Risikobewertung unter Heranziehung statistischer Erhebungen".
4.2. Zur Vermeidung nicht erlaubter Diskriminierung prüfen Aktuare, dass in Bezug auf die geltenden Vorschriften keine Variablen genutzt werden, die bei der Festlegung der Einzelwerte als explizit diskriminierend gelten (beispielsweise Geschlecht oder Nationalität), sowie dass die Verwendung externer Daten nicht zu einer Diskriminierung führt. Folgende Ansätze können dabei zur Überprüfung eingesetzt werden:

- Vermeidung: Diskriminierungsfreiheit spätestens beim Übergang vom Kalkulationsmodell zur expliziten Berechnung von Einzelwerten aufgrund der Konstruktion (kein Ausweis von diskriminierenden Einzelwerten bzw. durch Implementierung entsprechender Modellrestriktionen im Vorfeld)
- Plausibilisierung: Begründung nach Konstruktion (Aussagekraft aller verwendeten Variablen begründen)
- Validierung: Ex-Post Überprüfung der Angemessenheit (beispielsweise stichprobenartiger Vergleich der Prämien verschiedener Gruppen)
4.3. Kriterien zur Segmentierung müssen durch relevante und dem Risiko angemessene Ziele definiert werden. Durch Segmentierungskriterien darf bei der Berechnung der Einzelwerte keine Diskriminierung erfolgen.

## Page 10
# 5. Datenschutzbeauftragter 

5.1. Bei der Verarbeitung personenbezogener Daten sollten Aktuare, sofern Unklarheiten über die im Unternehmen geregelten Prozesse hinaus auftreten, immer mit dem Datenschutzbeauftragten zusammenarbeiten.
5.2. Aktuare, die die Funktion eines Datenschutzbeauftragten (DSB) wahrnehmen, stellen sicher, dass sie über die erforderlichen Kenntnisse und Fähigkeiten verfügen, um diese Funktion ordnungsgemäß auszuüben.

## Page 11
# 6. Verwendung von Modellen, Methoden und Tools im Umgang mit Daten 

6.1. Aktuaren ist bewusst, dass es Grenzen bei den verwendeten Modellen, Methoden und Tools gibt und es in ihrem Aufgabenbereich liegt, diese Grenzen zu untersuchen. Sie kommunizieren die Genauigkeit und Grenzen der verwendeten Modelle und die zugehörigen Modellfehler.
6.2. Aktuare verwenden und erstellen bewusst keine fehlerhaften und / oder falschen Modelle, Methoden und Tools. Sie stellen für diese Anleitungen zur Verfügung, in denen unter anderem auch deren Grenzen und Möglichkeiten aufgezeigt werden.
6.3. Aktuare ergreifen alle Maßnahmen, um die unsachgemäße Verwendung ihrer Modelle, Methoden und Tools zu begrenzen. Aktuare verpflichten sich, die Risiken zu begrenzen, die sich aus von ihnen erstellten Tools ergeben können, unabhängig davon wem diese zugänglich sind.
6.4. Aktuare führen gemäß Art. 3 der Standesregeln ${ }^{9}$ Qualitätssicherungsmaßnahmen für die Ergebnisse von Modellen, Methoden und Tools durch.
6.5. Stellen Aktuare im Rahmen von Qualitätssicherungsmaßnahmen fest, dass sie die Ergebnisse ihrer Methoden und Tools nicht validieren können, überprüfen sie die Modelle, Methoden und Tools und führen bei Bedarf Anpassungen durch.
6.6. Bei Verdacht auf die Verwendung von fehlerhaften und / oder falschen Tools in ihrem Arbeitsgebiet ergreifen Aktuare alle Maßnahmen, um die Interessen ihrer Arbeitgeber / ihres Auftraggebers, ihrer Kunden oder das Ansehen der Aktuare bzw. des Berufsstandes zu schützen.
6.7. Aktuare sind sich der Tatsache bewusst, dass Ergebnisse von Modellen, Methoden und Tools für Dritte nicht transparent und nachvollziehbar sein können. Deren Ergebnisse können als diskriminierend empfunden werden und ihre Verwendung kann bei Diskriminierung sogar verboten werden.
6.8. Verwendung von Systemen der Künstlichen Intelligenz (KI)

Aktuare stellen sicher, dass sie bei Verwendung von KI-Systemen die sieben Grundbedingungen für Vertrauenswürdige KI

- menschliches Handeln und Aufsicht
- technische Robustheit und Sicherheit
- Datenschutz und Datenverwaltung
- Transparenz
- Vielfalt, Nichtdiskriminierung und Fairness
- ökologisches und gesellschaftliches Wohlergehen
- Verantwortlichkeit
gemäß [1] bestmöglich einhalten.
7.11 Aktuare beachten, dass neben ihrer berufsständischen Verpflichtung zur Verantwortungsnahme über Ergebnisse (z.B. durch Validierung und backtesting) automatisierte Entscheidungen und Profiling durch KI nur eingeschränkt erlaubt sind. Insbesondere achten sie darauf, dass Entscheidungen

[^0]
[^0]:    ${ }^{9}$ Siehe Fußnote 5

## Page 12
mit rechtlicher Wirkung oder ähnlicher erheblicher Beeinträchtigung nicht nur automatisiert erfolgen dürfen.
7.12 Aktuare können Entscheidungen, die auf Grundlage von KI-Systemen getroffen wurden, nachvollziehen und erklären. Umgekehrt werden derartige Entscheidungen, die nicht erklärt und nachvollzogen werden können, nicht verwendet.

## Page 13
# Quellen 

[1] High-Level Expert Group on Artificial Intelligence, „Ethics guidelines for trustworthy AI," 8 April 2019. [Online]. Available: https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=58477.
[2] Deutsche Aktuarvereinigung (DAV) e.V., „Standesregeln für Aktuare in der Deutschen Aktuarvereinigung (DAV) e.V.," 25 April 2019. [Online]. Available: https://aktuar.de/regularien/2019-04-25_DAV-Standesregeln.pdf.
[3] unabhängige Datenschutzaufsichtsbehörden des Bundes und der Länder, „Hambacher Erklärung zur Künstlichen Intelligenz," 03 April 2019. [Online]. Available: https://www.datenschutzkonferenz-online.de/media/en/20190405_hambacher_erklaerung.pdf.
[4] Institut des Actuaires, „Norme de Pratique relative à l'utilisation et la protection des données massives, des données personnelles et des données de santé à caractère personnel," 16 November 2017. [Online]. Available: https://www.institutdesactuaires.com/global/gene/link.php?doc_id=11773. [Zugriff am 6 Dezember 2018].
[5] American Academy of Actuaries, „Big Data and the Role of the Actuary," 2018. [Online]. Available: https://www.actuary.org/files/publications/BigDataAndTheRoleOfTheActuary.pdf. [Zugriff am 13 Juni 2018].
[6] GDV, „Verhaltensregeln für den Umgang mit personenbezogenen Daten durch die deutsche Versicherungswirtschaft," 29 Juni 2018. [Online]. Available: https://www.gdv.de/resource/blob/23938/4aa2847df2940874559e51958a0bb350/download-code-of-conduct-data.pdf. [Zugriff am 22 Februar 2019].
[7] Europäische Union, „EUR-Lex," 27 April 2016. [Online]. Available: https://eur-lex.europa.eu/legalcontent/DE/TXT/PDF/?uri=CELEX:32016R0679\&from=DE. [Zugriff am 19 Juni 2019].