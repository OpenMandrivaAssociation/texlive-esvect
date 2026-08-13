%global tl_name esvect
%global tl_revision 77682
%global tl_version 1.3

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Write vectors using an arrow which differs from the Computer Modern one.
You have the choice between several kinds of arrows. The package
consists of the relevant Metafont code and a package to use it.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from esvect:
Map esvect.map
TL_DROPIN_EOF
