﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Inheritance3TablePerSubclass
{
    public class Pracownik : Osoba
    {
        public int Pensja { get; set; }
        public string Stanowisko { get; set; }
    }
}
