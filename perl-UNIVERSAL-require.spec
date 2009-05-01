%define module	UNIVERSAL-require
%define name	perl-%{module}
%define	modprefix UNIVERSAL
%define version	0.13
%define release	%mkrel 1

%define _provides_exceptions perl(UNIVERSAL)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Require modules from a variable
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Conflicts:	    perl-UNIVERSAL-exports < 0.03-3mdk
BuildRequires:	perl(Test::More) >= 0.47
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module creates a universal require() class method that will work with
every Perl module and is secure.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/UNIVERSAL
%{_mandir}/*/*


