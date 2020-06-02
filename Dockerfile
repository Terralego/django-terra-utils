FROM makinacorpus/geodjango:bionic-3.7

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pip3 install pip setuptools wheel -U
RUN python3.7 setup.py install
# Install dev requirements
RUN pip3 install -e .[dev]
