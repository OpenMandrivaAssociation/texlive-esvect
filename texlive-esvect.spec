%global tl_name esvect
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Vector arrows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esvect
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esvect.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Write vectors using an arrow which differs from the Computer Modern one.
You have the choice between several kinds of arrows. The package
consists of the relevant Metafont code and a package to use it.

