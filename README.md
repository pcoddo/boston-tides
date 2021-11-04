<!-- Header -->
![Header](https://raw.githubusercontent.com/pcoddo/boston-tides/main/img/header.png)

# Boston Tides
</p>
<p align="center">
    <em>Sea level rise and extreme value analysis for Boston IPCC AR6 Projections</em>
</p>

<!-- Badges -->
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/pcoddo/boston-tides?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/pcoddo/boston-tides)
![GitHub](https://img.shields.io/github/license/pcoddo/boston-tides)

## About
Python implementation of the sea level and storm surge analysis in Lempert et al. (2012) and [Oddo et al. (2017)](https://onlinelibrary.wiley.com/doi/full/10.1111/risa.12888). Generates sea level rise scenarios consistent with projections Chapter 9 of Working Group 1 contribution to the the IPCC Sixth Assessment Report.

Authors of original R code:
- [Klaus Keller ](https://personal.ems.psu.edu/~kzk10/)
- [Ryan Sriver](https://atmos.illinois.edu/directory/profile/rsriver)

**Contact:** [Perry Oddo](https://perryoddo.com)

## Installation

Clone repository to your device:
```shell
git init
```
```shell
git clone https://github.com/pcoddo/boston-tides.git
```

Create Anaconda environment using `environment.yml` file:
```shell
conda env create -f environment.yml
```

## Usage
The three Jupyter Notebooks describe how to run the code:
1. `ar6_fit_distribution.ipynb` Fits a lognormal distribution to the empirical sea level projections for Boston from the IPCC AR6.
![distribution](https://raw.githubusercontent.com/pcoddo/boston-tides/main/img/distribution.png)

2. `boston_slr.ipynb` Generates uncertain rejection sampling approach to generate uncertain sea level rise scenarios consistent with the IPCC expert assessment.
![projection](https://raw.githubusercontent.com/pcoddo/boston-tides/main/img/projection.png)

3. `boston_gev.ipynb` Performs a generalized extreme value (GEV) analysis for the Boston tide gauge using block maxima and Markov chain Monte Carlo.
![gev](https://raw.githubusercontent.com/pcoddo/boston-tides/main/img/gev.png)

## Cited works
- Lempert, R., Sriver, R. L., & Keller, K. (2012). Characterizing Uncertain Sea Level Rise Projections to Support Investment Decisions (No. CEC-500-2012-056). California Energy Commission Sacramento, CA, USA. Retrieved from http://ced.berkeley.edu/faculty/ratt/readings/ALL_THE_CLIMATE_PAPERS_2012/PoLA_revision_feb_28_2012.pdf

- Oddo, P. C., Lee, B. S., Garner, G. G., Srikrishnan, V., Reed, P. M., Forest, C. E., & Keller, K. (2017). Deep Uncertainties in Sea-Level Rise and Storm Surge Projections: Implications for Coastal Flood Risk Management. Risk Analysis. https://doi.org/10.1111/risa.12888


- Talke, S. A., Kemp, A. C., & Woodruff, J. (2018). Relative Sea Level, Tides, and Extreme Water Levels in Boston Harbor From 1825 to 2018. Journal of Geophysical Research: Oceans, 123(6), 3895–3914. https://doi.org/https://doi.org/10.1029/2017JC013645

- Fox-Kemper, B., H. T. Hewitt, C. Xiao, G. Aðalgeirsdóttir, S. S. Drijfhout, T. L. Edwards, N. R. Golledge, M. Hemer, R. E. Kopp, G. Krinner, A. Mix, D. Notz, S. Nowicki, I. S. Nurhati, L. Ruiz, J-B. Sallée, A. B. A. Slangen, Y. Yu, 2021, Ocean, Cryosphere and Sea Level Change. In: Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Masson-Delmotte, V., P. Zhai, A. Pirani, S. L. Connors, C. Péan, S. Berger, N. Caud, Y. Chen, L. Goldfarb, M. I. Gomis, M. Huang, K. Leitzell, E. Lonnoy, J. B. R. Matthews, T. K. Maycock, T. Waterfield, O. Yelekçi, R. Yu and B. Zhou (eds.)]. Cambridge University Press. In press.

- Garner, G. G., R. E. Kopp, T. Hermans, A. B. A. Slangen, G. Koubbe, M. Turilli, S. Jha, T. L. Edwards, A. Levermann, S. Nowikci, M. D. Palmer, C. Smith, in prep. Framework for Assessing Changes To Sea-level (FACTS). Geoscientific Model Development.

- Garner, G. G., T. Hermans, R. E. Kopp, A. B. A. Slangen, T. L. Edwards, A. Levermann, S. Nowikci, M. D. Palmer, C. Smith, B. Fox-Kemper, H. T. Hewitt, C. Xiao, G. Aðalgeirsdóttir, S. S. Drijfhout, T. L. Edwards, N. R. Golledge, M. Hemer, R. E. Kopp, G. Krinner, A. Mix, D. Notz, S. Nowicki, I. S. Nurhati, L. Ruiz, J-B. Sallée, Y. Yu, L. Hua, T. Palmer, B. Pearson, 2021. IPCC AR6 Sea-Level Rise Projections. Version 20210809. PO.DAAC, CA, USA. Dataset accessed [2021-10-26] at https://podaac.jpl.nasa.gov/announcements/2021-08-09-Sea-level-projections-from-the-IPCC-6th-Assessment-Report.

## Acknowledgements
We thank the projection authors for developing and making the sea-level rise projections available, multiple funding agencies for supporting the development of the projections, and the NASA Sea-Level Change Team for developing and hosting the IPCC AR6 Sea-Level Projection Tool. Special thanks to [Gregory Garner](https://sites.google.com/site/gggarner121) for providing subset of full projections for the Boston Tide gauge.


## Table of contents

<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [Project Title](#project-title)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
    - [Sponsor](#sponsor)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [License](#license)
- [Footer](#footer)

## Installation
[(^)](#table-of-contents)

<!-- *You might have noticed the **Back to top** button(if not, please notice, it's right there!). This is a good idea because it makes your README **easy to navigate.*** 

The first one should be how to install(how to generally use your project or set-up for editing in their machine).

This should give the users a concrete idea with instructions on how they can use your project repo with all the steps.

Following this steps, **they should be able to run this in their device.**

A method I use is after completing the README, I go through the instructions from scratch and check if it is working. -->

<!-- Here is a sample instruction:

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/navendu-pottekkat/nsfw-filter.git``` -->

## License
[MIT License](https://opensource.org/licenses/MIT)


[(Back to top)](#About)

