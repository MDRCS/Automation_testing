[![Generic badge](https://img.shields.io/badge/TDD-valide-<COLOR>.svg)](https://shields.io/)

# Automation_testing

    TIP :

    if you want to run tests each time on a whole folder for example `unit`
    go to `unittests in unit` -> `edit configuration` -> choose script path -> Target `/Users/MDRAHALI/Desktop/Learning_Roadmap/Automation_testing/TDD_Coding/tests/unit/
    pattern `*_test.py`` -> apply -> run tests


    - Unit test vs Intergration Test :

    Unit test is when you test one unit for example a class method
    Integration Test is when your test needs multiple classes and functions.

    TIP:

    to run all tests under the folder tests (unit, integration), go to `unittests in unit` -> `edit configuration`
    change target folder to -> Target `/Users/MDRAHALI/Desktop/Learning_Roadmap/Automation_testing/TDD_Coding/tests/
    apply -> run.


    %% Run Postman tests from pycharm - Advanced Config :

    install nvm
    $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    $ source ~/.bashrc
    $ nvm ls
    $ nvm ls-remote
    $ nvm install v14.4.0
    $ nvm use --delete-prefix v14.4.0
    $ npm i -g newman

    %% run tests just from command line :
    $ newman run stores-rest-api.postman_collection.json -e stores-rest-api.postman_environment.json

    %% configure newman on pytcharm
    % Step 1 - go to postman -> click on `manage environment` download environment (Store_Flask_REST_API)
    % Step 2 - go to pycharm preference -> click on plugins -> download `BashSupport` and `MultiRun`.
    % Step 3 - run app.py and stop it -> go to app above -> click on edit config -> click on the plus button `+` -> click on bash

         name : `Run newman tests`
         interpreter path : /usr/local/bin/newman
         program argument: stores-rest-api.postman_collection.json -e stores-rest-api.postman_environment.json
         working directory: /Users/MDRAHALI/Desktop/Learning_Roadmap/Automation_testing/flask_restful_api

    $ Apply and run

