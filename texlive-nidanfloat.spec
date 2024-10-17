Name:		texlive-nidanfloat
Version:	48295
Release:	2
Summary:	Bottom placement option for double float in two column mode (nidan-kumi)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nidanfloat
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nidanfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nidanfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nidanfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables a bottom placement option for double
floats in two column mode (nidan-kumi). It was originally part
of the Japanese pLaTeX bundle and is now distributed as a
separate package because it supports all LaTeX formats.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nidanfloat
%{_texmfdistdir}/tex/latex/nidanfloat
%doc %{_texmfdistdir}/doc/latex/nidanfloat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
