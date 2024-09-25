# TopFCNC4f

UFO model for top-quark FCNC simulation at NLO in QCD ([.zip](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fgdurieux%2FTopFCNC4f%2Ftree%2Fmaster%2FTopFCNC4f)).


It is derived from [TopFCNC](https://feynrules.irmp.ucl.ac.be/wiki/TopFCNC) by Céline Degrande with two modifications:
- four-fermion operators of `tuee/tuµµ/tuττ` and `tcee/tcµµ/tcττ` types have been added by hand, with the counterterms needed for NLO QCD simulation,
- the conventions for operator coefficients have been converted to that of [1802.07237](https://arxiv.org/abs/1802.07237).


Please refer to [1412.5594](https://arxiv.org/abs/1412.5594) and [1412.7166](https://arxiv.org/abs/1412.7166) if you use it.


Aside from the `TopFCNC4f` model itself, the other files provide elements of validation:
- by analytic comparison of Feynman rules against that of [TopFCNC](https://feynrules.irmp.ucl.ac.be/wiki/TopFCNC) and [dim6top](https://feynrules.irmp.ucl.ac.be/wiki/dim6top) models (see `.ipynb` and `.txt` files),
- by numerical comparison against Fig. 8 and 9 of [1412.7166](https://arxiv.org/abs/1412.7166) (see `.sh`, `.pdf`, `.svg` files)


Contact: Gauthier Durieux
