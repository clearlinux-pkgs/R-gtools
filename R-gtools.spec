#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gtools
Version  : 3.5.0
Release  : 39
URL      : http://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/gtools_3.5.0.tar.gz
Summary  : Various R Programming Tools
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gtools-lib
Requires: R-car
BuildRequires : R-car
BuildRequires : clr-R-helpers

%description
- assist in developing, updating, and maintaining R and R packages ('ask', 'checkRVersion',
    'getDependencies', 'keywords', 'scat'),
  - calculate the logit and inverse logit transformations ('logit', 'inv.logit'),
  - test if a value is missing, empty or contains only NA and NULL values ('invalid'),
  - manipulate R's .Last function ('addLast'),
  - define macros ('defmacro'),
  - detect odd and even integers ('odd', 'even'),
  - convert strings containing non-ASCII characters (like single quotes) to plain ASCII ('ASCIIfy'),
  - perform a binary search ('binsearch'),
  - sort strings containing both numeric and character components ('mixedsort'),
  - create a factor variable from the quantiles of a continuous variable ('quantcut'),
  - enumerate permutations and combinations ('combinations', 'permutation'),
  - calculate and convert between fold-change and log-ratio ('foldchange',
    'logratio2foldchange', 'foldchange2logratio'),
  - calculate probabilities and generate random numbers from Dirichlet distributions
    ('rdirichlet', 'ddirichlet'),
  - apply a function over adjacent subsets of a vector ('running'),
  - modify the TCP\_NODELAY ('de-Nagle') flag for socket objects,
  - efficient 'rbind' of data frames, even if the column names don't match ('smartbind'),
  - generate significance stars from p-values ('stars.pval'),
  - convert characters to/from ASCII codes.

%package lib
Summary: lib components for the R-gtools package.
Group: Libraries

%description lib
lib components for the R-gtools package.


%prep
%setup -q -c -n gtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502405736

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502405736
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gtools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gtools/ChangeLog
/usr/lib64/R/library/gtools/DESCRIPTION
/usr/lib64/R/library/gtools/INDEX
/usr/lib64/R/library/gtools/Meta/Rd.rds
/usr/lib64/R/library/gtools/Meta/data.rds
/usr/lib64/R/library/gtools/Meta/features.rds
/usr/lib64/R/library/gtools/Meta/hsearch.rds
/usr/lib64/R/library/gtools/Meta/links.rds
/usr/lib64/R/library/gtools/Meta/nsInfo.rds
/usr/lib64/R/library/gtools/Meta/package.rds
/usr/lib64/R/library/gtools/NAMESPACE
/usr/lib64/R/library/gtools/NEWS
/usr/lib64/R/library/gtools/R/gtools
/usr/lib64/R/library/gtools/R/gtools.rdb
/usr/lib64/R/library/gtools/R/gtools.rdx
/usr/lib64/R/library/gtools/data/ELISA.rda
/usr/lib64/R/library/gtools/help/AnIndex
/usr/lib64/R/library/gtools/help/aliases.rds
/usr/lib64/R/library/gtools/help/gtools.rdb
/usr/lib64/R/library/gtools/help/gtools.rdx
/usr/lib64/R/library/gtools/help/paths.rds
/usr/lib64/R/library/gtools/html/00Index.html
/usr/lib64/R/library/gtools/html/R.css
/usr/lib64/R/library/gtools/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gtools/libs/gtools.so
/usr/lib64/R/library/gtools/libs/gtools.so.avx2
