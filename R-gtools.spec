#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-gtools
Version  : 3.9.5
Release  : 105
URL      : https://cran.r-project.org/src/contrib/gtools_3.9.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gtools_3.9.5.tar.gz
Summary  : Various R Programming Tools
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gtools-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
  - modify the TCP_NODELAY ('de-Nagle') flag for socket objects,
  - efficient 'rbind' of data frames, even if the column names don't match ('smartbind'),
  - generate significance stars from p-values ('stars.pval'),
  - convert characters to/from ASCII codes ('asc', 'chr'),
  - convert character vector to ASCII representation ('ASCIIfy'),
  - apply title capitalization rules to a character vector ('capwords').

%package lib
Summary: lib components for the R-gtools package.
Group: Libraries

%description lib
lib components for the R-gtools package.


%prep
%setup -q -n gtools
pushd ..
cp -a gtools buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700511330

%install
export SOURCE_DATE_EPOCH=1700511330
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/gtools/NEWS.md
/usr/lib64/R/library/gtools/R/gtools
/usr/lib64/R/library/gtools/R/gtools.rdb
/usr/lib64/R/library/gtools/R/gtools.rdx
/usr/lib64/R/library/gtools/WORDLIST
/usr/lib64/R/library/gtools/data/ELISA.rda
/usr/lib64/R/library/gtools/data/badDend.rda
/usr/lib64/R/library/gtools/help/AnIndex
/usr/lib64/R/library/gtools/help/aliases.rds
/usr/lib64/R/library/gtools/help/figures/README-pressure-1.png
/usr/lib64/R/library/gtools/help/gtools.rdb
/usr/lib64/R/library/gtools/help/gtools.rdx
/usr/lib64/R/library/gtools/help/paths.rds
/usr/lib64/R/library/gtools/html/00Index.html
/usr/lib64/R/library/gtools/html/R.css
/usr/lib64/R/library/gtools/tests/smartbind_Dates.R
/usr/lib64/R/library/gtools/tests/smartbind_emptynames.R
/usr/lib64/R/library/gtools/tests/test_binsearch.R
/usr/lib64/R/library/gtools/tests/test_ddirichlet.R
/usr/lib64/R/library/gtools/tests/test_mixedorder.R
/usr/lib64/R/library/gtools/tests/test_script_file.R
/usr/lib64/R/library/gtools/tests/test_setTCPNoDelay.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gtools/libs/gtools.so
/usr/lib64/R/library/gtools/libs/gtools.so.avx2
/usr/lib64/R/library/gtools/libs/gtools.so.avx512
