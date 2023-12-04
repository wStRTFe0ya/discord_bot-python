# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Config:
	token: str = ''
	prefix: str = ''
