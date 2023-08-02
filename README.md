# ChatGPT ABAP Linter

This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well.

# Developer Setup

Developer setup for UNIX systems (Windows/WSL, Linux, Mac).

1. Clone this repository
2. Create a file named ***API-Key.env*** in the main directory containing your openai API key in the following format:
    ```
    OPENAI_KEY=<your API key>
    ```
3. Install all required python packages
4. Start the webserver inside the ./Webserver/ folder with `flask run`
5. Send a ***POST*** request to ***http://127.0.0.1:5000/linter*** containing a ***application/json*** body in the following format:
    ```
    {
        "programmingLanguage": "your Programming language",
        "code": "your code"
    }
    ```


# Directory Tree
```
.
├── ABAPExamples/                               - contains example code in ABAP
│   ├── zcl_abap_to_json.clas.abap              - used as a input
│   └── zcl_fs_ref_perf_testing.clas.abap       - used as a input
├── JSON/                                       - contains JSON files
│   ├── Layout.json                             - format for the GPT output
│   ├── LayoutTemplate.json                     - example GPT output
│   ├── client.json                             - example of POST request body
│   ├── exampleLint.json                        - was used as a few-shot prompt
│   ├── guessinggameLint.json                   - used as a few-shot prompt
│   └── openAPI.json                            - did describe the usage of the webserver according to the openAPI spec
├── PythonExamples/                             - contains example code in Python
│   ├── example.py                              - was used as a few-shot prompt
│   ├── guessinggame.py                         - used as a few-shot prompt
│   ├── heap.py                                 - used as an input
│   └── main.py                                 - used as an input
├── Webserver/                                  - 
│   └── app.py                                  - contains the flask webserver
├── .gitignore                                  - labels the files ignored by git
├── README.md                                   - this README
├── architecture.drawio.png                     - picture explaining the architecture 
├── dummielinter.py                             - just returns some message
├── jsonify.py                                  - script to convert code into the correct format for JSON
├── linter.py                                   - called by the flask server, sends requests to the openai API
├── message.py                                  - generates messages in the format used by the openai API
├── openapi.yml     	                        - describes the usage of the webserver according to the openAPI spec
├── prompts.txt                                 - contains different prompts
├── requirements.txt                            - pip requirements
└── test.py                                     - script that directly sends requests to the openai API
```

# Sources

- [guessinggame.py](https://codereview.stackexchange.com/questions/286118/guessing-game-in-python-which-uses-a-while-loop-with-3-guesses,)
- [example.py](https://www.codingem.com/python-linter/)
- [main.py](https://pythongeeks.org/python-calculator/)
- [heap.py](https://www.geeksforgeeks.org/python-program-for-heap-sort/)
- [ABAP examples/](https://github.com/SAP-samples/abap-oo-basics)


![](architecture.drawio.png)

# Todo

- [x] Python Code für's Prototyping verwenden
- [x] Few-Shot Prompt
- [x] JSON Validierung mit Retry

- [ ] Code Review vs "Linter"
- [ ] Dev Readme
- [ ] OpenAPI Spec erzeugen
- [ ] Dockerisieren des Webservers

## Future

- [ ] Iterative Ausgabe via generators()

## Erledigt

- [x] Random Seed - geht nicht
