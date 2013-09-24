%global packname  rms
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.0.0
Release:          1
Summary:          Regression Modeling Strategies
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rms_4.0-0.tar.gz
Requires:         R-Hmisc R-survival 
Requires:         R-survival 
Requires:         R-lattice R-quantreg R-nlme R-rpart R-polspline R-multcomp 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Hmisc R-survival
BuildRequires:    R-survival 
BuildRequires:    R-lattice R-quantreg R-nlme R-rpart R-polspline R-multcomp 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  rms is a collection of 229 functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models. rms works with almost
any regression model, but it was especially written to work with binary or
ordinal logistic regression, Cox regression, accelerated failure time
models, ordinary linear models, the Buckley-James model, generalized least
squares for serially or spatially correlated observations, generalized
linear models, and quantile regression.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/demo

