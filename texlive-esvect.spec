# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/esvect
# catalog-date 2006-10-27 00:09:51 +0200
# catalog-license gpl
# catalog-version 1.2
Name:		texlive-esvect
Version:	1.2
Release:	2
Summary:	Vector arrows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esvect
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Write vectors using an arrow which is different to the Computer
Modern one. You have the choice between several kinds of
arrows. The package consists of the relevant metafont code and
a package to use it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/esvect/esvect.map
%{_texmfdistdir}/fonts/source/public/esvect/mathvec.mf
%{_texmfdistdir}/fonts/source/public/esvect/vecsym.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect10.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect5.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect6.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect7.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect8.mf
%{_texmfdistdir}/fonts/source/public/esvect/vect9.mf
%{_texmfdistdir}/fonts/source/public/esvect/vsymbol.mf
%{_texmfdistdir}/fonts/tfm/public/esvect/vect10.tfm
%{_texmfdistdir}/fonts/tfm/public/esvect/vect5.tfm
%{_texmfdistdir}/fonts/tfm/public/esvect/vect6.tfm
%{_texmfdistdir}/fonts/tfm/public/esvect/vect7.tfm
%{_texmfdistdir}/fonts/tfm/public/esvect/vect8.tfm
%{_texmfdistdir}/fonts/tfm/public/esvect/vect9.tfm
%{_texmfdistdir}/fonts/type1/public/esvect/vect10.pfb
%{_texmfdistdir}/fonts/type1/public/esvect/vect5.pfb
%{_texmfdistdir}/fonts/type1/public/esvect/vect6.pfb
%{_texmfdistdir}/fonts/type1/public/esvect/vect7.pfb
%{_texmfdistdir}/fonts/type1/public/esvect/vect8.pfb
%{_texmfdistdir}/fonts/type1/public/esvect/vect9.pfb
%{_texmfdistdir}/tex/latex/esvect/esvect.sty
%{_texmfdistdir}/tex/latex/esvect/uesvect.fd
%doc %{_texmfdistdir}/doc/latex/esvect/README
%doc %{_texmfdistdir}/doc/latex/esvect/esvect.pdf
#- source
%doc %{_texmfdistdir}/source/latex/esvect/esvect.dtx
%doc %{_texmfdistdir}/source/latex/esvect/esvect.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751584
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718373
- texlive-esvect
- texlive-esvect
- texlive-esvect
- texlive-esvect

