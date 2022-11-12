Name:		texlive-greektex
Version:	28327
Release:	1
Summary:	Fonts for typesetting Greek/English documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/greektex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are based on Silvio Levy's classical Greek fonts;
macros and Greek hyphenation patterns for the fonts' encoding
are also provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/greektex/greektex.sty
%doc %{_texmfdistdir}/doc/fonts/greektex/README
%doc %{_texmfdistdir}/doc/fonts/greektex/gehyphw.gr
%doc %{_texmfdistdir}/doc/fonts/greektex/greektexdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/greektex/greektexdoc.tex
%doc %{_texmfdistdir}/doc/fonts/greektex/ywcl.zip

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
