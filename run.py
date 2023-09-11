#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import uvicorn
from main.factory import Main


app = Main.create_app()


if __name__ == "__main__":
    uvicorn.run("run:app", host='127.0.0.1', port=8083, reload=True, debug=True, workers=1)
