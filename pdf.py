def pdfspeaker(pdf):
    import pyttsx3,PyPDF2

    reader = PyPDF2.PdfReader(open(pdf, 'rb'))
    speaker = pyttsx3.init()

    all_text = ""

    for page_num in range(len(reader.pages)):
        text = reader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        all_text+= clean_text + " "

    speaker.save_to_file(all_text, 'pdf.mp3')
    speaker.runAndWait()

    speaker.stop()