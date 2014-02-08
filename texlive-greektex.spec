# revision 15878
# category Package
# catalog-ctan /fonts/greek/greektex
# catalog-date 2007-11-12 23:53:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-greektex
Version:	20071112
Release:	3
Summary:	Fonts for typesetting Greek/English documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/greektex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.doc.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/greektex/README
%doc %{_texmfdistdir}/doc/latex/greektex/gehyphw.gr
%doc %{_texmfdistdir}/doc/latex/greektex/greektexdoc.pdf
%doc %{_texmfdistdir}/doc/latex/greektex/greektexdoc.tex
%doc %{_texmfdistdir}/doc/latex/greektex/ywcl.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071112-2
+ Revision: 752432
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071112-1
+ Revision: 718582
- texlive-greektex
- texlive-greektex
- texlive-greektex
- texlive-greektex

